> Testo fornito dall'utente il 10/10/2026. Nomi di clienti, cantieri e imprese, indirizzi e importi sostituiti da segnaposto perché il repository è pubblico; gli originali restano fuori da git.

# RIEPILOGO — Progetto Claude "Rag system" (gestionale file e pratiche dello studio)
Periodo coperto: 29/08/2026 – 08/10/2026 · Riepilogo redatto il 10/10/2026
Fonte: chat del progetto + file di progetto (BASE_CONOSCENZA.md, ISTRUZIONI_PROGETTO.md, DECISIONI.md, PIANO_DI_LAVORO.md, IDEE_RACCOLTE.md).
Avvertenza: ricostruito da estratti di ricerca, non dalla lettura integrale di ogni chat.

> Testo incollato dall'utente nella sessione del 10/10/2026, riportato senza modifiche di contenuto.
> Sezioni: chat del progetto · 1 Contesto · 2 Struttura NAS · 3 File manager/mockup · 4 Pratiche studiate · 5 Script esistenti (con codice completo di struttura.py) · 6 Memorie/.md · 7 Decisioni · 8 Idee scartate · 9 Questioni aperte.

## Chat del progetto (per ritrovare il materiale)
| Data | Titolo chat | Argomento |
|---|---|---|
| 29/08 | Conformità normativa e checklist di verifica | checkbox di responsabilità, art. 1229/1341 c.c. |
| 30/08 | Multi-step AI workflow for data processing | cascata AI, SQL vs NoSQL, mockup checklist |
| 30/08 | Browser interface with clickable buttons and hover previews | interfaccia a bottoni, tipi di pratica |
| 01/09 | Statistical population of search results infographic | risultati correlati, "riprendi da qui" |
| 03/09 | DocFetcher vs regex comparison | DocFetcher come benchmark, visualizzatore OCR |
| 06/09 | Obsidian for architectural applications | sidecar .md, Obsidian |
| 11/09 | Procedura pratica per agibilità | caso [Cliente A], CFL, agibilità, ocr_ollama.py |
| 13/09 | n8n self-hosted setup | n8n sconsigliato |
| 13/09 | Extracting DockFetcher index data | costruisci_indice.py, ricerca.html |
| 15/09 | Urgent folder scan with file identification | triage.py, percorsi.py, schede.py, catalogo.py |
| 24/09 | Dock fetcher system with browser research | indice.py (ricerca da browser, server di rete) |
| 30/09 | Reorganizing file storage and folder structure | struttura NAS, struttura.py, pannello.py |
| 02/10 | Architectural studio folder organization | revisione struttura, modelli per tipo, PDF |
| 07/10 | Handling file save errors when file is open | Libera_File_NAS.bat |
| 08/10 | NAS server OS for i3 processor | OpenMediaVault, backup, accesso remoto, launcher |

---

## 1. CONTESTO

**Obiettivo, in due filoni:**
- **(a) Catalogo dell'archivio storico.** Circa 2000 documenti, Campania rurale, comuni multipli, tipi di pratica misti. Documenti raggruppati per immobile e pratica, con riassunto, metadati e apertura dell'originale. Posizionamento: "recupero e catalogazione dell'archivio storico", non un gestionale.
- **(b) Riorganizzazione operativa dello studio.** NAS, struttura cartelle, regole di nomenclatura, pannello per smistare i file, ricerca full-text da browser, backup.

**Fase:** whiteboard (istruzioni v2). Nessuna architettura del catalogo è decisa. Il materiale precedente vale come riferimento, non come vincolo.

**Persone citate:**
- Nicola: collaboratore, ha il problema WiFi peggiore e un laptop con file che nessun altro ha.
- Valentina: collaboratrice.
- Franco: architetto/studio ("studio Franco").
- Il numero "3 collaboratori" non risulta dalle chat → DA VERIFICARE.

**Problemi da risolvere:**
- Circa 1/3 dei documenti è senza livello di testo (scansioni).
- Nomi file inutili (`1.pdf`, `Documento 30.pdf`, `Scansione_001.pdf`).
- Duplicati: dalla scansione del backup di Nicola risultano ~41.500 file, 18% duplicati.
- Versioni gestite a mano con cartelle come `Ultimi` (254 volte), `Superati`, `V2` ecc. In totale il 17% delle cartelle.
- Nessun vocabolario per le sottocartelle: 437 sottocartelle di primo livello, 382 nomi diversi.
- File lasciati sul Desktop e nei Download.
- Condivisione Windows inaffidabile, cadute WiFi, file bloccati quando restano aperti su un altro PC.
- Documenti sensibili (codici fiscali, atti notarili, documenti d'identità) → responsabilità GDPR.

---

## 2. STRUTTURA NAS

**Hardware e sistema** (chat 08/10):
- Vecchio PC i3 con 8 GB di RAM.
- OS: OpenMediaVault (OMV), installato su chiavetta USB Kingston da 32 GB. Un HDD da 250 GB è stato scartato per settori danneggiati.
- Disco 2 TB = lavoro/condivisione. Disco 8 TB WD Purple = solo backup.
- Dischi formattati ext4. Migrazione dei dati con rsync.
- Indirizzo: `\\192.168.1.9\Nas`, mappato come `E:`.
- Condivisione SMB `NasHdd` con utenti separati.
- Nota: il nome della condivisione compare sia come `Nas` sia come `NasHdd` → DA VERIFICARE quale è attuale.

**Backup:**
- Cestino SMB.
- rsnapshot orario sul 2 TB: 24 orari, 7 giornalieri, 1 settimanale.
- Notturno sull'8 TB: 7 giornalieri, 4 settimanali, 24 mensili.
- Plugin openmediavault-rsnapshot e plugin writecache.

### Versione 1 — da `struttura.py` (30/09; l'utente: "the structure is ok")

Cartelle di base:
```
00_INBOX
01_CLIENTI
02_FORNITORI
03_STUDIO
99_CHIUSE
```

Sottocartelle di ogni lavoro:
```
00_Incarico
01_Immobile
02_Comune
03_Progetto
04_Lavori
05_Foto
06_Corrispondenza
99_Emessi
```

Regole (testo di LEGGIMI_STRUTTURA.txt):
- Ogni lavoro: `AAAA-NNN_Cliente_Descrizione` (es. `2026-014_Rossi_Via-Schiti`). Il numero non cambia mai.
- Percorso: `01_CLIENTI\Rossi_Mario\2026-001_Rossi_Via-Schiti\`
- Nomi dei file: `AAAA-MM-GG_Tipo-documento_v2.pdf`
- Vietati "finale", "definitivo", "nuovo2".
- Ciò che è stato inviato va in `99_Emessi` e non si modifica più.
- La numerazione riparte ogni anno (punto segnalato come da decidere).
- I caratteri vietati da Windows vengono tolti; gli accenti restano.

### Revisione (02/10) — PROPOSTA, non confermata

Critiche alla V1:
- Il cliente non è l'elemento stabile; lo è la particella.
- Lo stato legittimo richiede la storia dell'immobile.
- Spostare un lavoro in `99_CHIUSE` rompe i percorsi.
- Un incarico non coincide con una pratica.

Proposta A — Cliente → Lavoro → Pratiche:
```
NAS
├── 00_INBOX
├── 01_CLIENTI
│   └── [Cliente B]
│       └── 2022-007_[Cliente B]_Casandrino_Via-Roma
│           ├── _SCHEDA.txt         cliente · comune · foglio/particella · tipo · stato
│           ├── 00_Incarico
│           ├── 01_Immobile
│           ├── 02_Pratiche
│           │   ├── 01_CILAS_2022-03
│           │   │   ├── lavoro
│           │   │   └── trasmessi
│           │   │       └── 2022-03-15_CILAS_PEC
│           │   ├── 02_SAL-1_2022-09
│           │   └── 03_CFL_2023-01
│           ├── 03_Progetto
│           │   ├── CAD
│           │   └── PDF
│           ├── 04_Cantiere
│           ├── 05_Foto
│           └── 06_Corrispondenza
├── 02_FORNITORI
└── 03_STUDIO
```

V2 — modelli per tipo di lavoro (presentata come proposta principale nel PDF `Cartelle_strutture_predefinite_2026-10-02.pdf`):
- **Edilizia:** `00_IN-LAVORAZIONE · 01_Incarico · 02_Immobile-e-catasto · 03_Rilievo · 04_Progetto-CAD · 05_Titolo-edilizio · 06_Varianti-e-integrazioni · 07_Cantiere-DL · 08_Fine-lavori-Agibilita · 09_Foto · 99_TRASMESSI`
- **Catastale:** `00_IN-LAVORAZIONE · 01_Incarico · 02_Visure-e-planimetrie · 03_Rilievo · 04_DOCFA · 05_TM-Pregeo · 06_Volture · 07_Foto · 99_TRASMESSI`
- **Sicurezza:** `00_IN-LAVORAZIONE · 01_Incarico · 02_Documenti-impresa · 03_PSC · 04_POS · 05_Notifica-preliminare · 06_Verbali-coordinamento · 07_Foto · 99_TRASMESSI`
- **Perizia:** `00_IN-LAVORAZIONE · 01_Nomina-e-incarico · 02_Atti-di-causa · 03_Sopralluoghi · 04_Rilievo-e-catasto · 05_Perizia · 06_Foto · 99_TRASMESSI`
- **Strutturale:** `00_IN-LAVORAZIONE · 01_Incarico · 02_Rilievo-e-indagini · 03_Progetto-CAD · 04_Calcoli · 05_Genio-Civile · 06_Collaudo · 07_Foto · 99_TRASMESSI`
- **Piccolo** (APE, POS singolo…): `00_IN-LAVORAZIONE · Foto · 99_TRASMESSI`, con i file sciolti nel lavoro.

Altri punti della revisione:
- I modelli vivranno in un file di testo in `03_STUDIO\Modelli_cartelle`.
- Le date nei nomi vanno girate da `GG_MM_AA` a `AAAA-MM-GG`.
- Varianti sulle pratiche V1/V2/V3 → DA VERIFICARE nel PDF.
- Quale struttura sia definitiva → DA VERIFICARE / non decisa.

---

## 3. FILE MANAGER / MOCKUP

**File manager da browser con pannello sinistro/destro, drag&drop e modalità copia/indice:** nessuno trovato nelle chat di questo progetto → DA VERIFICARE (forse in un'altra chat o progetto).

Strumenti effettivamente prodotti:

**a) `pannello.py`** — Python, finestra desktop Tkinter; output in /mnt/user-data/outputs della chat 30/09.
- Nasce dall'alternativa "piccola app accanto a Esplora risorse". Un file manager completo da zero è stato sconsigliato.
- Riquadri dei lavori: legge `01_CLIENTI`, ogni utente fissa i propri lavori (lista salvata per utente).
- Trascina e smista: si trascina un file su un riquadro, si sceglie la sottocartella, il file viene spostato e rinominato con la data.
- Sorveglia i Download con il popup "Dove va?".
- Pulsanti: "Nuovo lavoro", "Aggiungi lavoro", "Annulla ultimo spostamento". "Chiudi lavoro" verso `99_CHIUSE` era stato solo proposto.
- Menu Altro → Posizione: "Sul desktop (dietro alle finestre)" (predefinita), "Sempre sopra a tutto", "Finestra normale".
- Al primo avvio chiede la cartella archivio (quella che contiene `01_CLIENTI`) e la verifica.
- Regole di sicurezza dichiarate: copia, verifica, poi rimuove l'originale; non cancella mai; tiene un log con annulla.
- Limite noto: se Chrome o Esplora sono massimizzati, non si può trascinare sul pannello.

**b) `indice.py` / `indicexl.py`** — Python, ricerca full-text nel browser (chat 24/09).
- Indice SQLite FTS5 (`indice.db`), server HTTP sulla porta 8777.
- Comandi: `index <cartella>`, `stima`, `doppioni`, `sposta`, `--rete`, `--silenzioso`.
- Pulsanti per ogni risultato: Apri, Mostra nella cartella, Da lavorare (copia in "Documenti da lavorare" senza sovrascrivere, aggiungendo `_2`).
- Da remoto: Copia percorso / Copia cartella, con traduzione in percorso di rete tramite `CONDIVISIONI`.
- Menu a tendina per filtrare per archivio indicizzato.
- `ESTENSIONI = {".pdf", ".p7m", ".docx", ".xlsx", ".xlsm"}`.
- I file senza testo vengono segnalati con una barra ambra ("trovato solo per nome file").
- Versione citata: v11.

**c) Mockup checklist pratica** — widget HTML nella chat 30/08.
- Schede "apertura"/"attuale", pallino verde/ambra/rosso (presente/illeggibile/assente).
- Al passaggio del mouse mostra un estratto di testo. Il click è simulato.

**d) Indice HTML statico precedente** — `indice.html`, tentativo precedente.
- Filtro per entità, selezione multipla, "Crea cartella di raccolta" tramite script .bat/.sh scaricato.

**e) Altri prototipi di ricerca:**
- `esempio_ricerca.html` / `ricerca.html` da `costruisci_indice.py` + `minisearch.js`.
- `verifica-ocr.html`, visualizzatore OCR adattato al telefono.

**f) Software già esistente valutato:** XYplorer, Directory Opus, Total Commander, One Commander, Q-Dir, Files, Double Commander. Consiglio: Nicola ne prova due per una settimana → esito DA VERIFICARE.

---

## 4. PRATICHE STUDIATE

Uno studio strutturato per CFL/CIL/CILA/SCIA (documenti obbligatori/facoltativi, dipendenze, parallelismi, scadenze, normativa, modulistica): **nessuno** nelle chat di questo progetto → DA VERIFICARE.

Materiale effettivamente presente:

**Caso [Cliente A] (chat 11/09) — pacchetto CFL trasmesso l'11/12/23, numerato dallo studio:**
```
00_ACCOMPAGNATORIA
01_ISTANZA_CFL
02_CAMERA_IMPRESA_ESECUTRICE
03_DURC_IMPRESA_ESECUTRICE
04_ANALISI_E_FORMULARIO_RIFIUTI
     ← 05 mancante (in entrambe le copie)
06_CERTIFICATO_REGOLARE_ESECUZIONE_E_ULTIMAZIONE_LAVORI
```
- Il contenuto del 05 va ricavato dall'accompagnatoria → DA VERIFICARE.
- Per nome non risultano: dichiarazioni di conformità impianti/DM 37, DoP, marcatura CE, schede tecniche di prodotto, certificati di posa.

**Agibilità [Cliente A], sub 5:**
- Ordine indicato: fine lavori → DOCFA → agibilità (SCA).
- La ricevuta DOCFA protocollata è allegato della SCA.
- Il DOCFA va chiuso: sub 5 accatastato F/3 dal 2022.
- L'agibilità va fatta da zero: mancano relazione asseverata, dichiarazioni di conformità impianti, APE del sub 5.

**DURC:** presente come documento (03 del pacchetto CFL). Validità/scadenza non discussa → DA VERIFICARE.

**Elenco tipi di pratica (chat 30/08, "da far correggere a Franco"):**
- PdC
- SCIA / SCIA alternativa
- CILA
- CILA Superbonus
- Bonus edilizi
- Condono/sanatoria (L.47/85, L.724/94, L.326/03)
- Agibilità
- Variante
- Autorizzazione paesaggistica
- DIA
- Collaudo statico
- Frazionamento/accatastamento
- Demolizione e ricostruzione
- Cambio di destinazione d'uso
- Piano attuativo

**Vocabolario dello studio:** CFL, SAL, ADE, CILAS, DNL, ASID, CIR. Il significato di DNL/ASID/CIR → DA VERIFICARE.

**Tipi di lavoro reali di Nicola** (dal backup): DOCFA, APE, POS/PSC, CILA/SCIA, CTU/CTP, sismica/dissesti, enti, clienti industriali ([clienti industriali]).

**Riferimenti normativi citati:**
- dPR 380/2001, artt. 20, 23, 24, 67 (in BASE_CONOSCENZA.md).
- Regolamento Edilizio Tipo e recepimento in Campania.
- Modulistica unificata.
- Artt. 1229 e 1341 c.c. (per la checklist).
- Modulistica regionale/comunale specifica: nessuna.

---

## 5. SCRIPT ESISTENTI

| File | Linguaggio | Cosa fa | Input → Output | Chat |
|---|---|---|---|---|
| `struttura.py` | Python | crea le cartelle base e i nuovi lavori numerati; senza `--crea` fa solo una prova | radice NAS, `--cliente`, `--nome`, `--anno` → cartelle + `LEGGIMI_STRUTTURA.txt` | 30/09 |
| `pannello.py` | Python (Tkinter) | pannello di smistamento (vedi §3) | file trascinati/scaricati → file spostati e rinominati, log | 30/09 |
| `indice.py` / `indicexl.py` | Python | indicizzazione e ricerca full-text, server web | cartelle → `indice.db`, pagina sulla porta 8777 | 24/09 |
| `costruisci_indice.py` (+`minisearch.js`) | Python + JS | indice di ricerca statico nel browser | cartella archivio → `ricerca.html` | 13/09 |
| `triage.py` | Python | inventario: formato reale (magic bytes), pagine/caratteri, tipo ipotizzato, regex | cartella → `triage.csv` | 15/09 |
| `percorsi.py` | Python | deduplica la coda OCR, classifica dai percorsi | `triage.csv` → `triage_percorsi.csv`, `da_ocr_dedup.txt` | 15/09 |
| `catalogo.py` | Python | raggruppa per cartella-pratica (tabella `PRATICHE` da correggere a mano), "DA ASSEGNARE" | cartella → catalogo (formato DA VERIFICARE) | 15/09 |
| `schede.py` | Python | riassunti via Ollama (`think: False`); gli identificativi restano alla regex | testo → `riassunti/` | 15/09 |
| `ocr_ollama.py` | Python | OCR tramite Ollama, default `glm-ocr`; marca le pagine `VUOTA` | cartella (es. `c:\nn`) → `.txt` per file | 11/09 |
| `Libera_File_NAS.bat` | Batch Windows | via SSH + `smbstatus`: file aperti, PC connessi, disconnessione sessione | IP NAS (192.168.1.9) → azioni sul NAS | 07/10 |
| Launcher web (nome DA VERIFICARE) + `cerca_particelle.py` | Python + systemd | avvia programmi dal browser, porte automatiche, chiusura dopo 30 min (+15); la chiave API Zornade è spostata in variabile d'ambiente | cartella `_programmi` → servizi web | 08/10 |
| `build_pdf3.py` | Python | genera il PDF delle strutture cartelle | → `Cartelle_strutture_predefinite_2026-10-02.pdf` | 02/10 |
| `verifica-ocr.html` | HTML/JS | visualizzatore OCR con colori di confidenza | `esempio_pratica.pdf` + `.hocr` | 03/09 |
| Tentativo precedente: `schema.py`, `extract.py`, `llm_index.py`, `catalog.py` (non funzionante), `indice.html`, `ingest.py`, `query.py` | Python/HTML | vedi PIANO_DI_LAVORO.md §10 | — | file di progetto |

Codice completo recuperato: solo `struttura.py`, nella versione del 30/09. Possibili modifiche successive → DA VERIFICARE. Il codice degli altri script va preso dalle chat indicate.

```python
#!/usr/bin/env python3
"""
struttura.py - crea la struttura cartelle dello studio e i nuovi lavori.

    python struttura.py init  \\\\192.168.1.9\\Nas                       prova
    python struttura.py init  \\\\192.168.1.9\\Nas --crea                crea le cartelle di base

    python struttura.py nuovo \\\\192.168.1.9\\Nas --cliente "Rossi Mario" --nome "Via Schiti"
    python struttura.py nuovo \\\\192.168.1.9\\Nas --cliente "Rossi Mario" --nome "Via Schiti" --crea

Senza --crea non scrive nulla: mostra solo cosa farebbe.
Non cancella e non sovrascrive mai. Se il numero e' gia' preso (anche da
un collega che sta creando un lavoro nello stesso momento) passa al successivo.
"""
import argparse
import os
import re
import sys
from datetime import date

CARTELLE_BASE = [
    "00_INBOX",
    "01_CLIENTI",
    "02_FORNITORI",
    "03_STUDIO",
    "99_CHIUSE",
]

SOTTOCARTELLE_LAVORO = [
    "00_Incarico",
    "01_Immobile",
    "02_Comune",
    "03_Progetto",
    "04_Lavori",
    "05_Foto",
    "06_Corrispondenza",
    "99_Emessi",
]

LEGGIMI = """STRUTTURA ARCHIVIO - regole in breve

00_INBOX      Arriva qui tutto quello che non ha ancora una casa. Si svuota ogni settimana.
01_CLIENTI    Un cartella per cliente, dentro una cartella per ogni lavoro.
02_FORNITORI  Contratti, listini, cataloghi. I documenti di un solo lavoro vanno nel lavoro.
03_STUDIO     Amministrazione, assicurazioni, modelli, carta intestata.
99_CHIUSE     Lavori finiti, in attesa di passare all'archivio.

Ogni lavoro: AAAA-NNN_Cliente_Descrizione  (es. 2026-014_Rossi_Via-Schiti)
Il numero non cambia mai, anche se il nome del cliente viene scritto in modi diversi.

Nomi dei file:  AAAA-MM-GG_Tipo-documento_v2.pdf
Niente "finale", "definitivo", "nuovo2". Cio' che e' stato inviato va in 99_Emessi e non si modifica piu'.
"""

VIETATI = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
NUM = re.compile(r"^(\d{4})-(\d{3})_")


def pulisci(testo, sep):
    """Toglie i caratteri che Windows non accetta e sistema gli spazi."""
    testo = VIETATI.sub("", testo).strip().strip(".")
    return re.sub(r"\s+", sep, testo)


def numeri_esistenti(radice, anno):
    """Numeri gia' usati nell'anno, cercando in 01_CLIENTI e 99_CHIUSE (2 livelli)."""
    usati = set()
    for base in ("01_CLIENTI", "99_CHIUSE"):
        top = os.path.join(radice, base)
        if not os.path.isdir(top):
            continue
        for livello1 in os.scandir(top):
            if not livello1.is_dir():
                continue
            m = NUM.match(livello1.name)
            if m and int(m.group(1)) == anno:
                usati.add(int(m.group(2)))
            for livello2 in os.scandir(livello1.path):
                if livello2.is_dir():
                    m = NUM.match(livello2.name)
                    if m and int(m.group(1)) == anno:
                        usati.add(int(m.group(2)))
    return usati


def cmd_init(a):
    if not os.path.isdir(a.radice):
        sys.exit(f"Non trovo la cartella: {a.radice}\nControlla di avere accesso al disco di rete.")
    for nome in CARTELLE_BASE:
        p = os.path.join(a.radice, nome)
        if os.path.isdir(p):
            print(f"  esiste gia'  {p}")
        elif a.crea:
            os.makedirs(p)
            print(f"  creata       {p}")
        else:
            print(f"  (prova) creerei  {p}")
    leggimi = os.path.join(a.radice, "LEGGIMI_STRUTTURA.txt")
    if not os.path.exists(leggimi):
        if a.crea:
            with open(leggimi, "w", encoding="utf-8") as f:
                f.write(LEGGIMI)
            print(f"  creato       {leggimi}")
        else:
            print(f"  (prova) creerei  {leggimi}")
    if not a.crea:
        print("\nProva finita. Aggiungi --crea per creare davvero.")


def cmd_nuovo(a):
    if not os.path.isdir(os.path.join(a.radice, "01_CLIENTI")):
        sys.exit("01_CLIENTI non esiste. Esegui prima:  python struttura.py init <disco> --crea")
    anno = a.anno or date.today().year
    cliente_cartella = pulisci(a.cliente, "_")
    cognome = cliente_cartella.split("_")[0]
    descrizione = pulisci(a.nome, "-")
    if not cliente_cartella or not descrizione:
        sys.exit("Cliente e nome del lavoro non possono essere vuoti.")

    usati = numeri_esistenti(a.radice, anno)
    n = max(usati) + 1 if usati else 1
    dir_cliente = os.path.join(a.radice, "01_CLIENTI", cliente_cartella)

    for _ in range(20):
        nome_lavoro = f"{anno}-{n:03d}_{cognome}_{descrizione}"
        dir_lavoro = os.path.join(dir_cliente, nome_lavoro)
        if not a.crea:
            print(f"(prova) creerei:\n  {dir_lavoro}")
            for s in SOTTOCARTELLE_LAVORO:
                print(f"    {s}")
            print("\nProva finita. Aggiungi --crea per creare davvero.")
            return
        os.makedirs(dir_cliente, exist_ok=True)
        try:
            os.mkdir(dir_lavoro)          # atomico: fallisce se qualcuno l'ha appena creato
        except FileExistsError:
            n += 1
            continue
        for s in SOTTOCARTELLE_LAVORO:
            os.mkdir(os.path.join(dir_lavoro, s))
        print(f"Creato: {dir_lavoro}")
        return
    sys.exit("Non riesco a trovare un numero libero. Riprova.")


def main():
    p = argparse.ArgumentParser(description="Struttura cartelle dello studio")
    sub = p.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init", help="crea le cartelle di base")
    i.add_argument("radice")
    i.add_argument("--crea", action="store_true", help="scrive davvero (senza: solo prova)")
    i.set_defaults(fn=cmd_init)

    n = sub.add_parser("nuovo", help="crea un nuovo lavoro")
    n.add_argument("radice")
    n.add_argument("--cliente", required=True)
    n.add_argument("--nome", required=True, help="es. 'Via Schiti'")
    n.add_argument("--anno", type=int)
    n.add_argument("--crea", action="store_true", help="scrive davvero (senza: solo prova)")
    n.set_defaults(fn=cmd_nuovo)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
```

---

## 6. MEMORIE / FILE .md

**`ISTRUZIONI_PROGETTO.md` (v1)**
- Brief del progetto catalogo.
- 8 vincoli: OCR come passo zero; tre stati; degradare in modo visibile; regex prima dell'LLM sugli identificativi; `comune` come chiave di instradamento; raggruppamento a due livelli; provenienza su ogni campo; checklist del professionista.
- Posizionamento, direzioni aperte, domande per l'architetto.

**Istruzioni v2 "fase whiteboard"** (testo incollato nel messaggio di oggi)
- Nessuna architettura decisa; il tentativo precedente è un input, non un'autorità.
- Restano vincolanti solo 5 fatti misurati: ~1/3 senza testo; 3 stati; checksum deterministico per CF/P.IVA; `comune` blocca se non estratto; particella con più pratiche da non fondere.
- Niente codice o architetture definitive finché la whiteboard non viene chiusa esplicitamente.

**`DECISIONI.md`** (tentativo precedente)
- D01–D14: catalogo e non verificatore; OCR prima di tutto; tre stati; regex batte LLM; due livelli; cascata di modelli; schemi piatti; HTML statico; OCR locale poi cloud; scansione incrementale con `_DA_INSERIRE`; versione su ogni riga; sidecar .md; grafo seminato; posizionamento.
- Sospese: checklist, MCP, ricerca semantica.
- Correzioni registrate: NuExtract3 è generativo; il clustering a chiave singola era un bug; `REQUIRED_TYPES` globale era sbagliato.

**`PIANO_DI_LAVORO.md`** (tentativo precedente)
- Risultati misurati su 20 documenti: 13 classificati a 0,95; 6 da OCR; 1 non classificato.
- Pipeline a 7 passi, cartella di consegna, indice HTML, modelli, OCR, ordine di costruzione, sidecar, grafo, funzionalità non validate, mercato (Magoot, NOVA, ProgettoFacile, GEC).

**`IDEE_RACCOLTE.md`** — idee della whiteboard senza status di decisione:
- checklist normativa fornita dal cliente vs checklist auto-referenziale (accompagnatoria);
- doppio controllo AI + umano;
- anteprima solo testuale;
- uno o più file fisici per documento (non deciso).

**`BASE_CONOSCENZA.md`** — cosa caricare nella knowledge del progetto e come nominarlo.

**Altri file:**
- `METADATA_STRATEGY.md`: citato, non presente tra i file di progetto → DA VERIFICARE.
- `LEGGIMI_STRUTTURA.txt` e `_SCHEDA.txt` sono file di istruzione/scheda, ma .txt (testo riportato in §2).

**Memoria Claude dell'account:** vuota.

---

## 7. DECISIONI PRESE

Confermate dall'utente:
- Disco 2 TB = lavoro/condivisione; 8 TB = solo backup.
- NAS con OpenMediaVault su i3.
- Struttura V1 di `struttura.py` approvata il 30/09 ("the structure is ok"), poi riaperta il 02/10.
- Archivi dal 2008 al 2019 probabilmente lasciati fuori per ora.
- Git/GitHub no per i documenti, sì solo per il codice.
- Risparmio energetico: solo spegnimento dei dischi; sospensione + Wake-on-LAN esclusi per affidabilità.
- `indice.py` legge solo pdf, p7m, docx, xlsx, xlsm.
- La funzione più importante dell'indice per Nicola è aprire la cartella del file.
- [Cliente A] è il caso di test giusto.

Fatti misurati vincolanti (istruzioni v2): vedi §6.

Raccomandazioni dell'assistente con adozione DA VERIFICARE:
- Tailscale per l'accesso remoto (CGNAT Vodafone).
- Nicola via cavo Ethernet; IP fisso per il NAS.
- Pannello piccolo invece di un file manager completo.

---

## 8. IDEE SCARTATE

| Idea | Perché | Scartata da |
|---|---|---|
| File manager completo da zero | anni di lavoro, rischio di perdere file in silenzio | consiglio assistente |
| Estrarre l'indice di DocFetcher | Lucene vecchio, niente testo leggibile, niente OCR; DocFetcher tenuto solo come termine di paragone | consiglio assistente |
| n8n per la pipeline | un lavoro batch non si adatta; licenza Sustainable Use; è un servizio da tenere attivo | consiglio assistente |
| "AI che copia e non riscrive" | nessun LLM è garantito estrattivo → regex + checksum | consiglio assistente (riprende D04) |
| LayoutLMv3 | licenza non commerciale, richiede etichettatura | tentativo precedente |
| gemma4 su GPU da 8 GB | non ci sta, rallentamento di 30× | tentativo precedente |
| Auto-compilazione della checklist da ricerca | stato cambiato senza conferma → sostituita da suggerimento + click di conferma | consiglio assistente |
| Checkbox singola come esonero di responsabilità | artt. 1229 e 1341 c.c.: serve approvazione specifica e separata | consiglio assistente |
| Desktop reindirizzato sul NAS | Windows si blocca se il NAS è lento o spento | consiglio assistente |
| Port forwarding / DDNS | impossibile con CGNAT | vincolo tecnico |
| Sospensione + Wake-on-LAN | affidabilità | utente |
| Git per i documenti | — | utente |
| Grafo globale | illeggibile con 2000 nodi | tentativo precedente |

---

## 9. QUESTIONI APERTE

- File manager da browser (pannelli, drag&drop, modalità copia/indice): dove è stato definito? → DA VERIFICARE.
- Studio delle pratiche CFL/CIL/CILA/SCIA (documenti, dipendenze, DURC, modulistica Campania/comuni): da fare o da recuperare.
- Struttura NAS definitiva:
  - V1 o Proposta A con `02_Pratiche`?
  - Modelli per tipo (V2)?
  - Numerazione annuale o continua?
  - Numerazione retroattiva dei lavori vecchi?
  - Rinunciare allo spostamento in `99_CHIUSE`?
- Tre domande a Nicola sui modelli: tipi mancanti, cartelle inutili, dove metterebbe 10 file veri.
- Domande aperte del progetto:
  - Il problema è *trovare* i documenti o *produrre* pacchi da consegnare?
  - Lo studio usa già un gestionale?
  - Quali funzioni proposte sono inutili?
- Catalogo: uno o più file fisici per documento (il blocco dei file spinge verso file separati); anteprima immagine sì/no.
- [Cliente A]: contenuto del documento 05 mancante nel pacchetto CFL; chiusura del DOCFA del sub 5; SCA da preparare.
- NAS:
  - completare l'installazione del launcher (servizio systemd, utente `programmi`, cartella `_programmi`);
  - accesso remoto (Tailscale?);
  - seconda copia off-site degli archivi vecchi;
  - nome della condivisione (`Nas` vs `NasHdd`).
- OCR: misurare i secondi per pagina e l'accuratezza di `glm-ocr` su scansioni italiane reali.
- Prova di XYplorer/Q-Dir da parte di Nicola: esito.
