#!/usr/bin/env python3
"""
crea_demo.py - costruisce esempio/demo.html: la stessa pagina dell'app, ma senza server.

L'archivio di esempio e i tipi di pratica sono scritti dentro la pagina; le chiamate /api/... vengono
servite da JavaScript in memoria. Serve per far provare l'interfaccia da un telefono o da un link.
Niente viene salvato: chiudendo la pagina si riparte da zero.
"""
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(QUI)
sys.path.insert(0, QUI)
from crea_esempio import ALBERO  # noqa: E402


def albero_json():
    radice = {}
    for cart, voci in ALBERO.items():
        nodo = radice
        for parte in cart.split("/"):
            nodo = nodo.setdefault("_d", {}).setdefault(parte, {})
        nodo["_f"] = [{"nome": n, "ext": n.rsplit(".", 1)[-1].lower(),
                       "modificato": n[:10] if re.match(r"\d{4}-\d{2}-\d{2}", n) else "2026-01-15", "dimensione": 12000} for n, _ in voci]
    return radice


def tipi_json():
    out = {}
    for n in sorted(os.listdir(os.path.join(REPO, "pratiche"))):
        if n.endswith(".json"):
            with open(os.path.join(REPO, "pratiche", n), encoding="utf-8") as f:
                t = json.load(f)
            out[t["sigla"]] = t
    return out


SHIM = r"""
<script>
window.DEMO=true;
(function(){
const ALBERO=__ALBERO__, TIPI=__TIPI__;
const S={pratiche:{}, ordine:[]};
const oggi=()=>new Date().toISOString().slice(0,10);
function nodo(p){let n=ALBERO;for(const parte of p.split("/").filter(Boolean)){n=(n._d||{})[parte];if(!n)throw new Error("cartella non trovata")}return n}
function albero(p){const n=nodo(p);return {percorso:p,cartelle:Object.keys(n._d||{}).sort(),file:(n._f||[]).slice().sort((a,b)=>b.modificato.localeCompare(a.modificato))}}
function fileInfo(p){const i=p.lastIndexOf("/");const n=nodo(p.slice(0,i));const f=(n._f||[]).find(x=>x.nome===p.slice(i+1));if(!f)throw new Error("file non trovato nell'archivio");return f}
const def=(t,c)=>{const d=TIPI[t].documenti.find(x=>x.codice===c);if(!d)throw new Error("documento sconosciuto");return d};
function crea(b){if(!TIPI[b.tipo])throw new Error("tipo sconosciuto");const cl=(b.cliente||"").trim().replace(/[<>:"/\\|?*]/g,"").replace(/\s+/g,"_");if(!cl)throw new Error("cliente vuoto");
  let id=`${cl}_${b.tipo}_${b.mese||oggi().slice(0,7)}`,n=2;const base=id;while(S.pratiche[id])id=`${base}_${n++}`;
  S.pratiche[id]={id,tipo:b.tipo,cliente:b.cliente.trim(),comune:(b.comune||"").trim(),mese:b.mese||oggi().slice(0,7),stato:"aperta",creata:oggi(),documenti:{},invii:[]};S.ordine.push(id);return {id}}
function collega(id,b){const p=S.pratiche[id];const d=def(p.tipo,b.codice);const manc=(d.prerequisiti||[]).filter(c=>!p.documenti[c]);if(manc.length)throw new Error("prima servono: "+manc.join(", "));
  const f=fileInfo(b.percorso);p.documenti[b.codice]={percorso:b.percorso,nome:f.nome,sha256:"demo"+Math.random().toString(16).slice(2,14),dimensione:f.dimensione,modificato:f.modificato+" 00:00",collegato_il:oggi(),da:"demo",validita_giorni:d.validita_giorni||undefined};return p}
function scollega(id,b){const p=S.pratiche[id];for(const c in p.documenti)if((def(p.tipo,c).prerequisiti||[]).includes(b.codice))throw new Error(c+" dipende da "+b.codice+": scollega prima quello");delete p.documenti[b.codice];return p}
const nomeStd=(p,c,n)=>`${oggi()}_${c}_${def(p.tipo,c).nome.replace(/[<>:"/\\|?*']/g,"").replace(/\s+/g,"-").slice(0,60)}.${n.split(".").pop()}`;
function copia(id){const p=S.pratiche[id];return {copiati:Object.entries(p.documenti).map(([c,v])=>(def(p.tipo,c).cartella||"03_tecnico")+"/"+nomeStd(p,c,v.nome))}}
function pacchetto(id){const p=S.pratiche[id],t=TIPI[p.tipo];return {pratica:{id,tipo:p.tipo,nome:t.nome,cliente:p.cliente,comune:p.comune,mese:p.mese},
  istruzioni:"Compila il modulo usando solo i dati dei documenti elencati, con la fonte per ogni valore. Ciò che manca va in lacune.",controlli_incrociati:t.controlli_incrociati||[],
  documenti:t.documenti.map(d=>{const v=p.documenti[d.codice];return v?{codice:d.codice,slot:d.nome,obbligatorio:d.obbligatorio,stato:"collegato",originale:v.percorso,leggi:null,nota:"da convertire in Markdown"}:{codice:d.codice,slot:d.nome,obbligatorio:d.obbligatorio,stato:"mancante"}}),generato:oggi()}}
function invio(id,b){const p=S.pratiche[id];const codici=(b.codici||[]).filter(c=>p.documenti[c]);if(!codici.length)throw new Error("nessun documento collegato da inviare");
  const data=b.data||oggi(),canale=(b.canale||"PEC").replace(/\s+/g,"-");const i={data,canale:b.canale||"PEC",protocollo:(b.protocollo||"").trim(),note:(b.note||"").trim(),codici,file:codici.map(c=>nomeStd(p,c,p.documenti[c].nome)),cartella:`99_TRASMESSI/${data}_${canale}`,registrato:oggi()};
  p.invii.push(i);const t=TIPI[p.tipo];if(t.documenti.filter(d=>d.obbligatorio===true).every(d=>p.documenti[d.codice]))p.stato="inviata";return i}
function indice(q){let voci=[];for(const id of S.ordine){const p=S.pratiche[id];for(const [c,v] of Object.entries(p.documenti)){const d=def(p.tipo,c);
  voci.push({cliente:p.cliente,comune:p.comune,tipo:p.tipo,pratica:id,mese:p.mese,anno:p.mese.slice(0,4),codice:c,documento:d.nome,ext:v.nome.split(".").pop().toLowerCase(),nome:v.nome,percorso:v.percorso,modificato:v.modificato,inviato:p.invii.some(i=>i.codici.includes(c)),produce:d.produce||""})}}
  for(const [k,val] of q)if(val)voci=voci.filter(x=>String(x[k]||"")===val);
  const faccette={};for(const k of ["cliente","comune","tipo","anno","documento","ext","produce"]){const m={};voci.forEach(x=>m[x[k]]=(m[x[k]]||0)+1);faccette[k]=Object.entries(m).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]))}
  voci.sort((a,b)=>b.modificato.localeCompare(a.modificato));return {faccette,voci:voci.slice(0,300),totale:voci.length}}
const elenco=()=>S.ordine.map(id=>{const p=S.pratiche[id];return {id,tipo:p.tipo,cliente:p.cliente,comune:p.comune,mese:p.mese,stato:p.stato}});
function rotta(url,opt){const u=new URL(url,"http://demo.locale/");const b=opt&&opt.body?JSON.parse(opt.body):{};const path=u.pathname.replace(/^.*\/api/,"/api");let m;
  if(path==="/api/config")return {archivio:"Archivio di esempio (dimostrazione)",pratiche:"pratiche_aperte",estensioni:[],tipi:TIPI};
  if(path==="/api/albero")return albero(u.searchParams.get("p")||"");
  if(path==="/api/pratiche")return opt&&opt.method==="POST"?crea(b):elenco();
  if(path==="/api/indice")return indice([...u.searchParams.entries()]);
  if(path==="/api/apri")return {percorso:b.percorso.replace(/\/[^/]+$/,""),nota:"nel programma vero si apre Esplora risorse"};
  if((m=path.match(/^\/api\/pratiche\/([^/]+)$/)))return S.pratiche[decodeURIComponent(m[1])]||(()=>{throw new Error("pratica non trovata")})();
  if((m=path.match(/^\/api\/pratiche\/([^/]+)\/(\w+)$/))){const id=decodeURIComponent(m[1]);if(!S.pratiche[id])throw new Error("pratica non trovata");return {collega,scollega,copia,pacchetto,invio}[m[2]](id,b)}
  throw new Error("non trovato: "+path)}
window.fetch=async(url,opt)=>{await new Promise(r=>setTimeout(r,30));try{const d=rotta(String(url),opt);return {ok:true,status:200,json:async()=>JSON.parse(JSON.stringify(d))}}catch(e){return {ok:false,status:400,statusText:e.message,json:async()=>({errore:e.message})}}};
// pratica di partenza, già avviata
crea({tipo:"CFL",cliente:"Rossi Mario",comune:"Avellino",mese:"2025-10"});
const R="01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/";
[["CFL-00",R+"02_Comune/2025-03-01_CILA_prot-1234.pdf"],["CFL-02",R+"04_Lavori/2025-10-02_Certificato-ultimazione-lavori.pdf"],["CFL-04","02_FORNITORI/Bianchi_Costruzioni/2025-09-20_DURC_Bianchi.pdf"],["CFL-05","02_FORNITORI/Bianchi_Costruzioni/2025-08-01_Visura-camerale_Bianchi.pdf"],["CFL-12",R+"02_Comune/2025-03-01_CILA_prot-1234.pdf"]].forEach(([c,p])=>{try{collega("Rossi_Mario_CFL_2025-10",{codice:c,percorso:p})}catch(e){}});
invio("Rossi_Mario_CFL_2025-10",{canale:"PEC",protocollo:"prot. 9999 del 2025-10-10",codici:["CFL-02","CFL-04"]});
crea({tipo:"CIL",cliente:"Verdi Anna",comune:"Benevento",mese:"2026-02"});
})();
</script>
"""


def main():
    with open(os.path.join(REPO, "app", "static", "index.html"), encoding="utf-8") as f:
        html = f.read()
    # la pagina pubblicata riceve già doctype/head/body: teniamo solo il contenuto
    head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
    head = re.sub(r"<meta[^>]*>\s*", "", head).strip()
    shim = SHIM.replace("__ALBERO__", json.dumps(albero_json(), ensure_ascii=False)).replace("__TIPI__", json.dumps(tipi_json(), ensure_ascii=False))
    avviso = ('<div style="background:var(--warn-soft);color:var(--warn);font-size:12.5px;padding:6px 12px;border-bottom:1px solid var(--line)">'
              "Versione dimostrativa: archivio inventato, niente viene salvato. Sul telefono: tocca un file, poi “Collega alla pratica”.</div>")
    out = head.replace("<title>Pratiche dello studio</title>", "<title>Pratiche dello studio – demo</title>") + "\n" + shim + "\n" + avviso + body
    out = out.replace("<style>", "<style>\nbody{display:flex;flex-direction:column}.app{flex:1;min-height:0}", 1)
    with open(os.path.join(QUI, "demo.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("scritto", os.path.join(QUI, "demo.html"), len(out) // 1024, "KB")


if __name__ == "__main__":
    main()
