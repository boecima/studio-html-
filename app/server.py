#!/usr/bin/env python3
"""
server.py - gestionale pratiche dello studio, da browser.

    python server.py                 pagina su http://127.0.0.1:8780 (solo questo PC)
    python server.py rete            raggiungibile dagli altri PC della rete
    python server.py --config x.json usa un altro file di configurazione

Solo libreria standard: niente pip install.
Legge l'archivio in sola lettura. Scrive solo nella cartella delle pratiche.
Non cancella mai un file dell'archivio.
"""
import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import stat
import sys
import urllib.parse
from datetime import date, datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE_REPO = os.path.dirname(QUI)
CONFIG = {}
TIPI = {}

ESTENSIONI_UFFICIO = {".pdf", ".p7m", ".doc", ".docx", ".xls", ".xlsx", ".xlsm", ".dwg", ".dxf",
                      ".jpg", ".jpeg", ".png", ".txt", ".md", ".odt", ".ods"}
VIETATI = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


# ----------------------------------------------------------------- utilità
def carica_config(percorso):
    with open(percorso, encoding="utf-8") as f:
        c = json.load(f)
    for k in ("archivio", "pratiche"):
        c[k] = os.path.abspath(os.path.join(os.path.dirname(percorso), c[k])) if not os.path.isabs(c[k]) else c[k]
    c.setdefault("estensioni", sorted(ESTENSIONI_UFFICIO))
    c.setdefault("tipi", os.path.join(RADICE_REPO, "pratiche"))
    c["tipi"] = c["tipi"] if os.path.isabs(c["tipi"]) else os.path.abspath(os.path.join(os.path.dirname(percorso), c["tipi"]))
    c.setdefault("porta", 8780)
    return c


def carica_tipi(cartella):
    tipi = {}
    for nome in sorted(os.listdir(cartella)):
        if nome.endswith(".json"):
            with open(os.path.join(cartella, nome), encoding="utf-8") as f:
                t = json.load(f)
            tipi[t["sigla"]] = t
    return tipi


def pulisci(testo, sep="_"):
    testo = VIETATI.sub("", str(testo)).replace("'", "").replace("’", "").strip().strip(".")
    return re.sub(r"\s+", sep, testo)


def dentro(base, rel):
    """Percorso assoluto di `rel` dentro `base`, oppure None se esce dalla cartella."""
    rel = (rel or "").replace("\\", "/").lstrip("/")
    p = os.path.realpath(os.path.join(base, rel))
    base = os.path.realpath(base)
    if p == base or p.startswith(base + os.sep):
        return p
    return None


def impronta(percorso, blocco=1 << 20):
    h = hashlib.sha256()
    with open(percorso, "rb") as f:
        while True:
            b = f.read(blocco)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def info_file(p):
    st = os.stat(p)
    return {"dimensione": st.st_size, "modificato": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")}


def oggi():
    return date.today().isoformat()


# ----------------------------------------------------------------- pratiche
def elenco_pratiche():
    base = CONFIG["pratiche"]
    out = []
    if not os.path.isdir(base):
        return out
    for nome in sorted(os.listdir(base)):
        pj = os.path.join(base, nome, "pratica.json")
        if os.path.isfile(pj):
            with open(pj, encoding="utf-8") as f:
                p = json.load(f)
            out.append({"id": nome, "tipo": p["tipo"], "cliente": p["cliente"], "comune": p.get("comune", ""),
                        "mese": p.get("mese", ""), "stato": p.get("stato", "aperta")})
    return out


def cartella_pratica(pid):
    p = dentro(CONFIG["pratiche"], pid)
    if not p or not os.path.isfile(os.path.join(p, "pratica.json")):
        raise FileNotFoundError("pratica non trovata")
    return p


def leggi_pratica(pid):
    with open(os.path.join(cartella_pratica(pid), "pratica.json"), encoding="utf-8") as f:
        return json.load(f)


def salva_pratica(pid, p):
    p["aggiornata"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(os.path.join(cartella_pratica(pid), "pratica.json"), "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    scrivi_indice(pid, p)


def crea_pratica(dati):
    tipo = dati["tipo"]
    if tipo not in TIPI:
        raise ValueError("tipo sconosciuto")
    cliente = pulisci(dati["cliente"])
    if not cliente:
        raise ValueError("cliente vuoto")
    mese = dati.get("mese") or date.today().strftime("%Y-%m")
    pid = f"{cliente}_{tipo}_{mese}"
    base = CONFIG["pratiche"]
    os.makedirs(base, exist_ok=True)
    cart = os.path.join(base, pid)
    n = 2
    while os.path.exists(cart):
        cart = os.path.join(base, f"{pid}_{n}")
        n += 1
    pid = os.path.basename(cart)
    os.mkdir(cart)
    for s in TIPI[tipo]["cartelle"]:
        os.mkdir(os.path.join(cart, s))
    p = {"id": pid, "tipo": tipo, "cliente": dati["cliente"].strip(), "comune": dati.get("comune", "").strip(),
         "mese": mese, "stato": "aperta", "creata": datetime.now().strftime("%Y-%m-%d %H:%M"),
         "documenti": {}, "invii": []}
    with open(os.path.join(cart, "pratica.json"), "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    scrivi_indice(pid, p)
    return pid


def doc_def(tipo, codice):
    for d in TIPI[tipo]["documenti"]:
        if d["codice"] == codice:
            return d
    raise ValueError("documento sconosciuto: " + codice)


def prerequisiti_mancanti(p, codice):
    d = doc_def(p["tipo"], codice)
    return [c for c in d.get("prerequisiti", []) if c not in p["documenti"]]


def collega(pid, codice, percorso_rel, forza=False):
    p = leggi_pratica(pid)
    d = doc_def(p["tipo"], codice)
    ass = dentro(CONFIG["archivio"], percorso_rel)
    if not ass or not os.path.isfile(ass):
        raise FileNotFoundError("file non trovato nell'archivio")
    manc = prerequisiti_mancanti(p, codice)
    if manc and not forza:
        raise PermissionError("prima servono: " + ", ".join(manc))
    # un file sta in un solo slot
    for k, v in list(p["documenti"].items()):
        if v["percorso"] == percorso_rel.replace("\\", "/") and k != codice:
            del p["documenti"][k]
    inf = info_file(ass)
    voce = {"percorso": percorso_rel.replace("\\", "/"), "nome": os.path.basename(ass), "sha256": impronta(ass),
            "dimensione": inf["dimensione"], "modificato": inf["modificato"], "collegato_il": oggi(),
            "da": os.environ.get("USERNAME") or os.environ.get("USER") or ""}
    if d.get("validita_giorni"):
        voce["validita_giorni"] = d["validita_giorni"]
    p["documenti"][codice] = voce
    salva_pratica(pid, p)
    return p


def scollega(pid, codice):
    p = leggi_pratica(pid)
    # non si scollega un documento che è prerequisito di uno già collegato
    for c, v in p["documenti"].items():
        if codice in doc_def(p["tipo"], c).get("prerequisiti", []):
            raise PermissionError(f"{c} dipende da {codice}: scollega prima quello")
    p["documenti"].pop(codice, None)
    salva_pratica(pid, p)
    return p


def nome_standard(p, codice, nome_orig):
    d = doc_def(p["tipo"], codice)
    ext = os.path.splitext(nome_orig)[1].lower()
    return f"{oggi()}_{codice}_{pulisci(d['nome'], '-')[:60]}{ext}"


def scrivi_indice(pid, p):
    """INDICE.md leggibile accanto a pratica.json: dove sta ogni documento."""
    t = TIPI[p["tipo"]]
    righe = [f"# {t['sigla']} · {p['cliente']} · {p.get('comune','')} · {p['mese']}", "",
             f"Aggiornato: {p.get('aggiornata', p.get('creata',''))}  ·  Archivio: `{CONFIG['archivio']}`", "",
             "| Codice | Documento | Stato | File nell'archivio | Modificato | SHA-256 |", "|---|---|---|---|---|---|"]
    for d in t["documenti"]:
        v = p["documenti"].get(d["codice"])
        obb = {True: "obbl.", False: "facolt.", "condizionato": "cond."}[d["obbligatorio"]]
        if v:
            righe.append(f"| {d['codice']} | {d['nome']} ({obb}) | collegato | `{v['percorso']}` | {v['modificato']} | {v['sha256'][:12]}… |")
        else:
            righe.append(f"| {d['codice']} | {d['nome']} ({obb}) | mancante | | | |")
    if p.get("invii"):
        righe += ["", "## Inviati", "", "| Data | Canale | Protocollo | Documenti | Cartella |", "|---|---|---|---|---|"]
        for i in p["invii"]:
            righe.append(f"| {i['data']} | {i['canale']} | {i.get('protocollo','')} | {', '.join(i['codici'])} | `{i['cartella']}` |")
    with open(os.path.join(cartella_pratica(pid), "INDICE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(righe) + "\n")


def copia(pid):
    """Uscita 2: copia dei file collegati nella cartella della pratica, con nome standard."""
    p = leggi_pratica(pid)
    cart = cartella_pratica(pid)
    fatti = []
    for codice, v in p["documenti"].items():
        d = doc_def(p["tipo"], codice)
        src = dentro(CONFIG["archivio"], v["percorso"])
        dst_dir = os.path.join(cart, d.get("cartella") or TIPI[p["tipo"]]["cartelle"][0])
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, nome_standard(p, codice, v["nome"]))
        if not os.path.exists(dst) or impronta(dst) != v["sha256"]:
            shutil.copy2(src, dst)
        v["copia"] = os.path.relpath(dst, cart).replace("\\", "/")
        fatti.append(v["copia"])
    salva_pratica(pid, p)
    return fatti


def pacchetto_ai(pid):
    """Uscita 3: manifest.json + testi leggibili per l'AI, in 05_pacchetto_ai (o nell'ultima cartella non TRASMESSI)."""
    p = leggi_pratica(pid)
    t = TIPI[p["tipo"]]
    cart = cartella_pratica(pid)
    nome_dir = next((c for c in t["cartelle"] if "pacchetto" in c.lower()), "pacchetto_ai")
    out = os.path.join(cart, nome_dir)
    os.makedirs(out, exist_ok=True)
    docs = []
    for d in t["documenti"]:
        v = p["documenti"].get(d["codice"])
        if not v:
            docs.append({"codice": d["codice"], "slot": d["nome"], "obbligatorio": d["obbligatorio"], "stato": "mancante"})
            continue
        src = dentro(CONFIG["archivio"], v["percorso"])
        ext = os.path.splitext(src)[1].lower()
        voce = {"codice": d["codice"], "slot": d["nome"], "obbligatorio": d["obbligatorio"], "stato": "collegato",
                "originale": v["percorso"], "sha256": v["sha256"], "modifica_originale": False}
        if ext in (".txt", ".md"):
            dst = os.path.join(out, d["codice"] + ".md")
            shutil.copyfile(src, dst)
            voce["leggi"] = os.path.relpath(dst, cart).replace("\\", "/")
        else:
            voce["leggi"] = None
            voce["nota"] = "da convertire in Markdown con converti_in_md.py (PDF/Word/Excel/p7m)"
        docs.append(voce)
    manifest = {"pratica": {"id": pid, "tipo": p["tipo"], "nome": t["nome"], "cliente": p["cliente"], "comune": p.get("comune", ""), "mese": p["mese"]},
                "istruzioni": "Compila il modulo della pratica usando solo i dati che trovi nei documenti elencati. Ogni valore con la fonte (codice documento e pagina). Non inventare: ciò che manca va in lacune.",
                "controlli_incrociati": t.get("controlli_incrociati", []),
                "documenti": docs, "generato": datetime.now().strftime("%Y-%m-%d %H:%M")}
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    return manifest


def registra_invio(pid, dati):
    """Inviati: copia immutabile di ciò che è partito, con data, canale e protocollo."""
    p = leggi_pratica(pid)
    t = TIPI[p["tipo"]]
    cart = cartella_pratica(pid)
    codici = [c for c in dati.get("codici", []) if c in p["documenti"]]
    if not codici:
        raise ValueError("nessun documento collegato da inviare")
    data = dati.get("data") or oggi()
    canale = pulisci(dati.get("canale") or "PEC", "-")
    nome_dir = next((c for c in t["cartelle"] if "trasmess" in c.lower() or "emess" in c.lower()), "99_TRASMESSI")
    dst_dir = os.path.join(cart, nome_dir, f"{data}_{canale}")
    n = 2
    while os.path.exists(dst_dir):
        dst_dir = os.path.join(cart, nome_dir, f"{data}_{canale}_{n}")
        n += 1
    os.makedirs(dst_dir)
    file_inviati = []
    for c in codici:
        v = p["documenti"][c]
        src = dentro(CONFIG["archivio"], v["percorso"])
        dst = os.path.join(dst_dir, nome_standard(p, c, v["nome"]))
        shutil.copy2(src, dst)
        os.chmod(dst, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)   # sola lettura: quello che è partito non si tocca
        file_inviati.append(os.path.basename(dst))
    invio = {"data": data, "canale": dati.get("canale") or "PEC", "protocollo": dati.get("protocollo", "").strip(),
             "note": dati.get("note", "").strip(), "codici": codici, "file": file_inviati,
             "cartella": os.path.relpath(dst_dir, cart).replace("\\", "/"), "registrato": datetime.now().strftime("%Y-%m-%d %H:%M")}
    p.setdefault("invii", []).append(invio)
    if all(d["codice"] in p["documenti"] for d in t["documenti"] if d["obbligatorio"] is True):
        p["stato"] = "inviata"
    salva_pratica(pid, p)
    return invio


def indice_globale(filtri):
    """Scheda Indice: faccette cliccabili su tutte le pratiche. Nessuna ricerca per testo."""
    voci = []
    for pr in elenco_pratiche():
        p = leggi_pratica(pr["id"])
        t = TIPI[p["tipo"]]
        for codice, v in p["documenti"].items():
            d = doc_def(p["tipo"], codice)
            voci.append({"cliente": p["cliente"], "comune": p.get("comune", ""), "tipo": p["tipo"], "pratica": pr["id"],
                         "mese": p["mese"], "anno": p["mese"][:4], "codice": codice, "documento": d["nome"],
                         "ext": os.path.splitext(v["nome"])[1].lower().lstrip("."), "nome": v["nome"],
                         "percorso": v["percorso"], "cartella": os.path.dirname(v["percorso"]), "modificato": v["modificato"],
                         "inviato": any(codice in i["codici"] for i in p.get("invii", [])), "produce": d.get("produce", "")})
    for k, val in filtri.items():
        if val:
            voci = [x for x in voci if str(x.get(k, "")) == val]
    faccette = {}
    for k in ("cliente", "comune", "tipo", "anno", "documento", "ext", "produce"):
        conta = {}
        for x in voci:
            conta[x[k]] = conta.get(x[k], 0) + 1
        faccette[k] = sorted(conta.items(), key=lambda kv: (-kv[1], kv[0]))
    voci.sort(key=lambda x: x["modificato"], reverse=True)
    return {"faccette": faccette, "voci": voci[:300], "totale": len(voci)}


def albero(rel):
    base = dentro(CONFIG["archivio"], rel)
    if not base or not os.path.isdir(base):
        raise FileNotFoundError("cartella non trovata")
    cartelle, file = [], []
    est = set(CONFIG["estensioni"])
    with os.scandir(base) as it:
        for e in it:
            if e.name.startswith((".", "~$", "_")):
                continue
            if e.is_dir():
                cartelle.append(e.name)
            elif e.is_file() and os.path.splitext(e.name)[1].lower() in est:
                st = e.stat()
                file.append({"nome": e.name, "ext": os.path.splitext(e.name)[1].lower().lstrip("."),
                             "modificato": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d"), "dimensione": st.st_size})
    cartelle.sort(key=str.lower)
    file.sort(key=lambda f: f["modificato"], reverse=True)
    return {"percorso": rel.replace("\\", "/").strip("/"), "cartelle": cartelle, "file": file}


# ----------------------------------------------------------------- http
class Gestore(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *a):
        if not CONFIG.get("silenzioso"):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % a))

    def _json(self, dati, stato=200):
        corpo = json.dumps(dati, ensure_ascii=False).encode("utf-8")
        self.send_response(stato)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def _errore(self, e, stato=400):
        self._json({"errore": str(e)}, stato)

    def _file(self, percorso, inline=True):
        if not os.path.isfile(percorso):
            return self._errore("file non trovato", 404)
        tipo = mimetypes.guess_type(percorso)[0] or "application/octet-stream"
        if percorso.lower().endswith((".md", ".txt")):
            tipo = "text/plain; charset=utf-8"
        with open(percorso, "rb") as f:
            corpo = f.read()
        self.send_response(200)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Content-Disposition", ("inline" if inline else "attachment") + '; filename="%s"' % os.path.basename(percorso))
        self.end_headers()
        self.wfile.write(corpo)

    def _corpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        try:
            if u.path == "/":
                return self._file(os.path.join(QUI, "static", "index.html"))
            if u.path.startswith("/static/"):
                p = dentro(os.path.join(QUI, "static"), u.path[len("/static/"):])
                return self._file(p) if p else self._errore("no", 404)
            if u.path == "/api/config":
                return self._json({"archivio": CONFIG["archivio"], "pratiche": CONFIG["pratiche"], "estensioni": CONFIG["estensioni"],
                                   "tipi": {k: {"sigla": t["sigla"], "nome": t["nome"], "descrizione": t.get("descrizione", ""),
                                                "norma": t.get("norma", ""), "stato_scheda": t.get("stato_scheda", ""),
                                                "cartelle": t["cartelle"], "documenti": t["documenti"],
                                                "controlli_incrociati": t.get("controlli_incrociati", []), "dopo": t.get("dopo", [])}
                                            for k, t in TIPI.items()}})
            if u.path == "/api/albero":
                return self._json(albero(q.get("p", "")))
            if u.path == "/api/file":
                p = dentro(CONFIG["archivio"], q.get("p", ""))
                return self._file(p) if p else self._errore("fuori dall'archivio", 403)
            if u.path == "/api/file_pratica":
                cart = cartella_pratica(q.get("id", ""))
                p = dentro(cart, q.get("p", ""))
                return self._file(p) if p else self._errore("fuori dalla pratica", 403)
            if u.path == "/api/pratiche":
                return self._json(elenco_pratiche())
            m = re.match(r"^/api/pratiche/([^/]+)$", u.path)
            if m:
                return self._json(leggi_pratica(urllib.parse.unquote(m.group(1))))
            if u.path == "/api/indice":
                return self._json(indice_globale({k: q.get(k, "") for k in ("cliente", "comune", "tipo", "anno", "documento", "ext", "produce")}))
            self._errore("non trovato", 404)
        except FileNotFoundError as e:
            self._errore(e, 404)
        except PermissionError as e:
            self._errore(e, 409)
        except Exception as e:
            self._errore(e, 500)

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        try:
            dati = self._corpo()
            if u.path == "/api/pratiche":
                return self._json({"id": crea_pratica(dati)}, 201)
            m = re.match(r"^/api/pratiche/([^/]+)/(collega|scollega|copia|pacchetto|invio)$", u.path)
            if m:
                pid, az = urllib.parse.unquote(m.group(1)), m.group(2)
                if az == "collega":
                    return self._json(collega(pid, dati["codice"], dati["percorso"], bool(dati.get("forza"))))
                if az == "scollega":
                    return self._json(scollega(pid, dati["codice"]))
                if az == "copia":
                    return self._json({"copiati": copia(pid)})
                if az == "pacchetto":
                    return self._json(pacchetto_ai(pid))
                if az == "invio":
                    return self._json(registra_invio(pid, dati), 201)
            if u.path == "/api/apri":
                p = dentro(CONFIG["archivio"], dati.get("percorso", ""))
                if not p:
                    return self._errore("fuori dall'archivio", 403)
                cart = p if os.path.isdir(p) else os.path.dirname(p)
                if sys.platform.startswith("win") and self.client_address[0] in ("127.0.0.1", "::1"):
                    os.startfile(cart)  # noqa: solo sul PC che ospita il server
                    return self._json({"aperta": cart})
                return self._json({"percorso": cart, "nota": "apri questa cartella da Esplora risorse"})
            self._errore("non trovato", 404)
        except FileNotFoundError as e:
            self._errore(e, 404)
        except PermissionError as e:
            self._errore(e, 409)
        except (KeyError, ValueError) as e:
            self._errore(e, 400)
        except Exception as e:
            self._errore(e, 500)


def main():
    global CONFIG, TIPI
    ap = argparse.ArgumentParser(description="Gestionale pratiche dello studio")
    ap.add_argument("modo", nargs="?", default="locale", choices=["locale", "rete"])
    ap.add_argument("--config", default=os.path.join(QUI, "config.json"))
    ap.add_argument("--porta", type=int)
    ap.add_argument("--silenzioso", action="store_true")
    a = ap.parse_args()
    if not os.path.isfile(a.config):
        sys.exit(f"Manca {a.config}. Copia config.esempio.json in config.json e scrivi i percorsi.")
    CONFIG = carica_config(a.config)
    CONFIG["silenzioso"] = a.silenzioso
    if not os.path.isdir(CONFIG["archivio"]):
        sys.exit(f"Non trovo l'archivio: {CONFIG['archivio']}")
    os.makedirs(CONFIG["pratiche"], exist_ok=True)
    TIPI = carica_tipi(CONFIG["tipi"])
    porta = a.porta or CONFIG["porta"]
    host = "0.0.0.0" if a.modo == "rete" else "127.0.0.1"
    print(f"Archivio (sola lettura): {CONFIG['archivio']}")
    print(f"Pratiche (scrittura):    {CONFIG['pratiche']}")
    print(f"Tipi di pratica:         {', '.join(TIPI)}")
    print(f"Pagina:                  http://{'<ip-di-questo-pc>' if a.modo == 'rete' else '127.0.0.1'}:{porta}   (Ctrl+C per chiudere)")
    try:
        ThreadingHTTPServer((host, porta), Gestore).serve_forever()
    except KeyboardInterrupt:
        print("\nChiuso.")


if __name__ == "__main__":
    main()
