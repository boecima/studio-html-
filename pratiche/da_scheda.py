#!/usr/bin/env python3
"""
da_scheda.py - genera pratiche/<sigla>.json dalla tabella "3. Documenti del pacchetto" di docs/pratiche/<nome>.md

    python pratiche/da_scheda.py            rigenera tutti i JSON dalle schede
    python pratiche/da_scheda.py cfl        solo una scheda

La scheda di ricerca è la fonte; il JSON è ciò che legge l'app. Se cambia la scheda, si rilancia questo script.
Le parole chiave per il suggerimento automatico e la sottocartella vengono ricavate dal nome del documento e da chi lo produce;
si possono forzare in pratiche/_extra.json (per codice).
"""
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
SCHEDE = os.path.join(os.path.dirname(QUI), "docs", "pratiche")
EXTRA = os.path.join(QUI, "_extra.json")

# parole che, se compaiono nel nome del documento, diventano parole chiave per riconoscere i file
ALIAS = {
    "durc": ["durc"], "visura camerale": ["visura", "camerale", "cciaa"], "visura catastale": ["visura"],
    "docfa": ["docfa", "catast"], "pregeo": ["pregeo", "mappale", "frazionamento"], "ape": ["ape", "attestato prestazione"],
    "identit": ["identita", "carta", "ci_"], "procura": ["procura", "delega"], "conformità impianti": ["conformita", "dm37", "dm 37", "impiant"],
    "conformita impianti": ["conformita", "dm37", "impiant"], "rifiuti": ["fir", "formulario", "rifiuti"],
    "ultimazione": ["ultimazione", "fine lavori", "fine-lavori"], "collaudo": ["collaudo"], "regolare esecuzione": ["regolare", "cre"],
    "fotograf": ["foto", "jpg"], "stato finale": ["stato finale", "stato-finale", "as built", "finale"],
    "elaborati grafici": ["tav", "elaborat", "pianta", "prospett", "sezion"], "relazione tecnica": ["relazione"],
    "relazione geologica": ["geolog"], "relazione geotecnica": ["geotec"], "relazione di calcolo": ["calcol"],
    "piano di manutenzione": ["manutenzione"], "materiali": ["materiali"], "notifica preliminare": ["notifica", "preliminare"],
    "polizza": ["polizza", "assicura", "rc"], "contratto": ["contratto", "appalto"], "organico": ["organico", "ccnl"],
    "modulo": ["modulo", "istanza"], "ricevuta": ["ricevuta", "protocollo", "prot"], "diritti": ["diritti", "bollettino", "pagopa", "versamento"],
    "titolo": ["cila", "cilas", "scia", "permesso", "pdc", "titolo"], "planimetria": ["planimetria"], "acustic": ["acustic"],
    "barriere": ["barriere", "dm236", "accessibilit"], "paesaggist": ["paesagg"], "legge 10": ["legge10", "legge 10", "l10", "ex l10"],
    "nomina": ["nomina", "accettazione", "incarico"], "accompagnamento": ["accompagnatoria", "accompagnamento", "lettera"],
    "varianti": ["variante", "varianti"], "sismic": ["sismic", "genio", "deposito"], "catena dei titoli": ["verifica", "titoli"],
}
CARTELLA_PER_RUOLO = [("committente", "01_committente"), ("impresa", "02_impresa"), ("tecnico", "03_tecnico"),
                      ("collaudatore", "03_tecnico"), ("geologo", "03_tecnico"), ("certificatore", "03_tecnico"),
                      ("installat", "02_impresa"), ("sue", "04_ente"), ("comune", "04_ente"), ("genio", "04_ente"),
                      ("agenzia", "04_ente"), ("ente", "04_ente"), ("soprintend", "04_ente")]


def celle(riga):
    return [c.strip() for c in riga.strip().strip("|").split("|")]


def obbligatorio(testo):
    t = testo.lower()
    if t.startswith("sì") or t.startswith("si") and not t.startswith("sia"):
        return True, ""
    if t.startswith("no"):
        return False, ""
    if t.startswith("condizionato"):
        cond = re.sub(r"^condizionato\s*:?\s*", "", testo, flags=re.I).strip()
        return "condizionato", cond
    return "condizionato", testo


def validita(testo):
    t = testo.lower()
    m = re.search(r"(\d+)\s*(gg|giorni)", t)
    if m and ("validit" in t or "dalla" in t or "richiesta" in t or "120" in t or "90" in t):
        return int(m.group(1))
    m = re.search(r"(\d+)\s*mes[ei]", t)
    if m and "validit" not in t and ("mesi" in t):
        return int(m.group(1)) * 30
    m = re.search(r"(\d+)\s*anni", t)
    if m and "valid" in t:
        return int(m.group(1)) * 365
    return None


def parole_chiave(nome):
    n = nome.lower()
    out = []
    for k, v in ALIAS.items():
        if k in n:
            out += v
    if not out:  # parole lunghe del nome, come ripiego
        out = [w for w in re.findall(r"[a-zàèéìòù]{6,}", n)][:4]
    return sorted(set(out))


def cartella(produce):
    p = produce.lower()
    trovati = [(p.find(k), c) for k, c in CARTELLA_PER_RUOLO if k in p]
    return min(trovati)[1] if trovati else "03_tecnico"


def leggi_scheda(percorso):
    with open(percorso, encoding="utf-8") as f:
        righe = f.read().splitlines()
    titolo = next((r for r in righe if r.startswith("# ")), "# ? — ?")[2:]
    m = re.match(r"\s*([A-Z]{2,6})\s*[—–-]\s*(.+)", titolo)
    sigla, nome = (m.group(1), m.group(2).strip()) if m else (os.path.basename(percorso)[:-3].upper(), titolo)
    in3, docs = False, []
    for r in righe:
        if r.startswith("## 3"):
            in3 = True
            continue
        if in3 and r.startswith("## "):
            break
        if in3 and r.startswith("|") and not r.startswith("|---") and not r.lower().startswith("| codice"):
            c = celle(r)
            if len(c) < 8 or not re.match(r"^[A-Z]{2,6}-\d{1,3}$", c[0]):
                continue
            obb, cond = obbligatorio(c[2])
            pre = re.findall(r"[A-Z]{2,6}-\d{1,3}", c[3]) if "tutti" not in c[3].lower() else []
            d = {"codice": c[0], "nome": c[1], "obbligatorio": obb}
            if cond:
                d["condizione"] = cond
            d.update({"prerequisiti": [p for p in pre if p != c[0]], "gruppo": c[4].replace("—", "").strip() or None,
                      "produce": c[5], "validita_giorni": validita(c[6]), "validita_testo": c[6] if c[6] not in ("—", "-", "") else "",
                      "nome_file": c[7], "fonte": c[8] if len(c) > 8 else "", "parole_chiave": parole_chiave(c[1]), "cartella": cartella(c[5])})
            if "tutti" in c[3].lower():
                d["prerequisiti_tutti"] = True
            docs.append(d)
    # sezione 7 (controlli) e 8 (collegamenti) come elenchi
    def sezione(n):
        out, dentro = [], False
        for r in righe:
            if r.startswith(f"## {n}"):
                dentro = True
                continue
            if dentro and r.startswith("## "):
                break
            r = r.strip()
            if not dentro or not r:
                continue
            if re.match(r"^([-*]|\d+\.)\s+", r):
                out.append(re.sub(r"^([-*]|\d+\.)\s+", "", r))
            elif re.search(r"\(\d+\)", r):      # "Errori tipici: (1) ... (2) ..."
                out += [x.strip(" ;.") for x in re.split(r"\s*\(\d+\)\s*", r) if x.strip(" ;.")]
            else:
                out.append(r)
        return out
    return sigla, nome, docs, sezione(7), sezione(8)


def controlla(docs):
    """Prerequisiti verso codici inesistenti e cicli: la scheda va corretta, non il JSON."""
    codici = {d["codice"] for d in docs}
    errori = [f"{d['codice']}: prerequisito {p} non esiste" for d in docs for p in d["prerequisiti"] if p not in codici]
    stato = {}
    def visita(c, pila):
        if c in pila:
            errori.append("ciclo: " + " → ".join(pila + [c]))
            return
        if stato.get(c):
            return
        for p in next(d for d in docs if d["codice"] == c)["prerequisiti"]:
            if p in codici:
                visita(p, pila + [c])
        stato[c] = True
    for d in docs:
        visita(d["codice"], [])
    return errori


def genera(nome_scheda):
    percorso = os.path.join(SCHEDE, nome_scheda + ".md")
    sigla, nome, docs, controlli, dopo = leggi_scheda(percorso)
    if not docs:
        print(f"  {nome_scheda}: nessuna tabella documenti, salto")
        return
    extra = {}
    if os.path.isfile(EXTRA):
        with open(EXTRA, encoding="utf-8") as f:
            extra = json.load(f)
    for d in docs:
        d["prerequisiti"] = [p for p in d["prerequisiti"] if any(x["codice"] == p for x in docs)]
        if d.get("prerequisiti_tutti"):
            prima = docs[:docs.index(d)]
            d["prerequisiti"] = [x["codice"] for x in prima if x["obbligatorio"] is True]
        d.update(extra.get(d["codice"], {}))
    sigle = []
    for d in docs:
        s_ = d["codice"].split("-")[0]
        if s_ not in sigle:
            sigle.append(s_)
    for s_ in sigle:
        ds = [d for d in docs if d["codice"].startswith(s_ + "-")]
        for d in ds:
            d["prerequisiti"] = [p for p in d["prerequisiti"] if any(x["codice"] == p for x in ds)]
        errori = controlla(ds)
        for e in errori:
            print(f"  ATTENZIONE {s_}: {e}")
        cartelle = sorted({d["cartella"] for d in ds}) + ["05_pacchetto_ai", "99_TRASMESSI"]
        nome_json = nome_scheda if s_ == sigla else s_.lower()
        out = {"sigla": s_, "nome": nome if s_ == sigla else f"{s_} (variante di {sigla}: vedi la scheda {nome_scheda}.md)",
               "descrizione": f"Vedi docs/pratiche/{nome_scheda}.md", "norma": "",
               "stato_scheda": f"generato da docs/pratiche/{nome_scheda}.md con pratiche/da_scheda.py; la scheda è una bozza da verificare con il tecnico",
               "cartelle": cartelle, "documenti": ds, "controlli_incrociati": controlli, "dopo": dopo}
        with open(os.path.join(QUI, nome_json + ".json"), "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"  {nome_json}.json: {len(ds)} documenti" + (f", {len(errori)} avvisi" if errori else ""))


def main():
    nomi = sys.argv[1:] or sorted(n[:-3] for n in os.listdir(SCHEDE) if n.endswith(".md") and not n.startswith("_"))
    for n in nomi:
        genera(n)


if __name__ == "__main__":
    main()
