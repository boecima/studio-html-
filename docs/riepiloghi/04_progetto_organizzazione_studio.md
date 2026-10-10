> Testo fornito dall'utente il 10/10/2026. Nomi di clienti, cantieri e imprese, indirizzi e importi sostituiti da segnaposto perché il repository è pubblico; gli originali restano fuori da git.

# RIEPILOGO – Progetto Claude "organizzazione studio" (Studio Arch. Nicola Franco)
Chat di riferimento: "Claude code vs desktop differences" (08/10/2026) + note di progetto (08–09/10/2026)
+ file di progetto RIEPILOGO_impostazione_2026-10-08.md. Riepilogo redatto il 10/10/2026.

---

## 1. CONTESTO

**Obiettivo**
- Web app usata solo da browser, installata sul server di casa/studio con OpenMediaVault (OMV).
- Gestisce le "pratiche" (job) come una checklist di documenti richiesti.
- I file dell'archivio vengono **collegati** (link), mai copiati.
- Alla fine, il pacchetto di link e testi va a un'AI che estrae le informazioni e redige la documentazione (es. CIL – comunicazione inizio lavori).

**Contesto più ampio** (dal file RIEPILOGO del 08/10)
- Organizzazione dello studio con l'AI: Cowork, Claude Code, Hermes, script Python.
- La cartella `Z:\Studio_AI` è l'unica scritta dall'AI.
- Il resto dell'archivio è in sola lettura.

**Utenti**
- Tony: organizza gli strumenti.
- Arch. Nicola Franco: usa la checklist e sceglie i file.
- Numero di collaboratori ("3 collaboratori"): non è mai stato detto qui. DA VERIFICARE.

**Problemi da risolvere**
- Evitare copie duplicate dei file.
- Avere una checklist dei documenti per tipo di pratica.
- Visualizzare i file in anteprima prima di collegarli.
- Dare all'AI un formato leggero (Markdown) per spendere meno token.
- Definire una struttura cartelle fissa sul server, partendo dalle abitudini di Nicola.

**Hardware**
- Vecchio i3 con 8 GB di RAM, con OpenMediaVault.
- Ci girano già altri piccoli programmi Python.

---

## 2. STRUTTURA NAS

### 2a. Struttura `Z:\Studio_AI` (definita nel file RIEPILOGO, riportata com'è)
```
Z:\Antonio\...  e  \\ADMINISTRATOR\Desktop\...     archivio dello studio – SOLA LETTURA per l'AI
Z:\Studio_AI\                                       unica cartella scritta dall'AI (in Ubuntu: /mnt/z/Studio_AI)
  .hermes.md = CLAUDE.md                            regole per Hermes e Claude Code (sempre identici)
  PSC_StudioFranco_pacchetto\                       libreria: 00 guida/lezioni/checklist · 01 librerie json · 02 script ·
                                                    03 modelli Word · 04 skill · 05 hermes · 06 organizzazione
  Cantieri\<Cognome_Nome>\originali | md | PSC_v2 | Stato_PSC_*.md
  Pratiche\<Tipo>_<Cognome>_<AAAA-MM>\
  _organizzazione\BACHECA.md · CONVENZIONI.md · pulizia_settimanale.py · rapporti\
```
- Copia d'origine del pacchetto: `Z:\Antonio\PSC [Cantiere A]\PSC_StudioFranco_pacchetto\`

### 2b. Struttura cartelle del server di studio (in progettazione; dalle note)
- Struttura per lo più fissa: cliente → lavoro → sottocartelle (CIL ecc.), più le cartelle "studio" e "modulistica".
- Archivio organizzato **PER CLIENTE**, non per lavoro (correzione del 09/10/2026).
- Nomi delle cartelle secondo la nomenclatura preferita da Nicola.
- Date nei nomi in formato **GG_MM_AA** (abitudine di Nicola).
- Il lavoro 110 % è quasi tutto chiuso e va in archivio.
- Le cartelle personali di Nicola vanno fuori dalla struttura dello studio, in una cartella separata.
- Metodo: prima si scansiona l'HDD di Nicola (il desktop `\\ADMINISTRATOR\Desktop`) per ricavare un prototipo della sua organizzazione, poi si progetta la struttura del server.
- L'albero completo **non è ancora stato definito** in questo progetto. DA VERIFICARE se esiste in Cowork.

### 2c. Struttura cartella pratica nel mockup (proposta, NON confermata)
```
Cantieri/<Cliente>_<TIPO>_<AAAA-MM>/
  ├─ 01_client_documents
  ├─ 02_contractors
  ├─ 03_drawings
  └─ 04_ai_package
```

**Incoerenze di nomenclatura – DA VERIFICARE**
- `Pratiche\<Tipo>_<Cognome>_<AAAA-MM>` (RIEPILOGO) contro `Cantieri/<Cliente>_<TIPO>_<AAAA-MM>` (mockup).
- Date AAAA-MM contro GG_MM_AA (abitudine di Nicola).
- Sottocartelle in inglese nel mockup contro la nomenclatura italiana di Nicola.

---

## 3. FILE MANAGER / MOCKUP

**Layout:** pagina sempre a due pannelli, con divisore trascinabile. Su telefono i pannelli si impilano.

**Pannello sinistro: Archivio (sola lettura)**
- Albero "vecchio stile" con caselle +/– e linee tratteggiate.
- Caricamento lazy: il contenuto di una cartella si carica solo quando la si apre.
- Per ogni cartella si vedono i 4 file modificati più di recente, più il link "show all N files".
- Badge colorato per estensione (PDF, DOCX, XLSX, DWG, JPG).
- ✓ verde sui file già collegati alla pratica.
- Puntino ambra sui file che, dal nome, sembrano adatti a uno slot vuoto (parole chiave tipo "durc", "visura").

**Anteprima**
- Clic su un file → l'anteprima si apre sopra il pannello destro.
- Sotto l'anteprima: menu per scegliere lo slot e pulsante "Link to job".
- Nel mockup l'anteprima è una pagina finta.

**Pannello destro: Lavori (job workspace)**
- Selettore della pratica e pulsante "New job".
- La finestra "New job" chiede tipo (CIL/CFL), cognome del cliente e mese, poi crea la cartella con 4 sottocartelle.
- Checklist di slot, ognuno marcato required/optional; lo slot diventa verde quando è riempito.
- Barra di avanzamento ("X of Y required documents").
- "Remove link" per scollegare un file da uno slot.

**Drag & drop:** si trascina un file dall'albero su uno slot. Un file si collega a un solo slot per pratica.

**Modalità copia/indice**
- Solo indice/link: l'originale non viene mai copiato.
- Il "link" è una riga nel database che punta al percorso originale.
- Una modalità "copia" non è prevista.

**Pacchetto per l'AI:** quando tutti i documenti obbligatori sono collegati, il pulsante "Prepare package for AI" mostra il `manifest.json`.

**Tecnologia del mockup:** un unico file HTML/CSS/JavaScript, senza framework, con dati di esempio.

**Tecnologia proposta per l'app reale** (proposta, non confermata):
- Python + FastAPI, SQLite, HTML con Alpine.js o htmx, griglia CSS a due colonne.
- Porta diversa dalla 80 di OMV (es. 8080).
- App eseguita come utente normale, con accesso in sola lettura all'archivio.
- Login con password; accesso da fuori solo via VPN (Tailscale/WireGuard).
- Opzione A (venv + servizio systemd) oppure Opzione B (Docker via omv-extras): **non scelta**. DA VERIFICARE.

**Modello dati proposto (SQLite, 4 tabelle)**

| Tabella | Contenuto |
|---|---|
| job_types | CIL, CFL, SCIA e altri tipi |
| required_documents | per tipo: documenti richiesti, ciascuno obbligatorio o facoltativo |
| jobs | cliente, tipo, data, stato, percorso cartella |
| job_files | pratica, slot, percorso originale, chi e quando |

- Estensione proposta per `job_files`: `md_path`, `converted_at`, `status` (ok / failed / needs OCR).
- Le checklist devono essere modificabili da browser.

**Manifest proposto (per slot)**
```json
{
  "slot": "Final works report",
  "read": "04_ai_package/relazione_tecnica.md",
  "original": "Archivio/Clienti/Rossi_Mario/Elaborati/relazione_tecnica.docx",
  "edit_original": false
}
```

**Ordine di sviluppo proposto**
1. Pagina a due pannelli con albero lazy e anteprima PDF/immagini.
2. Creazione pratica con cartelle e checklist.
3. Collegamento dei file agli slot, con avanzamento.
4. Esportazione del pacchetto per l'AI.
5. Conversioni, avvisi ed extra.

**Idee per dopo**
- Avvisi sui documenti mancanti.
- Controllo notturno dei file spostati o cancellati.
- Suggerimenti automatici in base al nome del file.
- Registro di chi ha collegato cosa e quando.
- L'app scrive solo nelle cartelle delle pratiche, mai nell'archivio.

**File prodotti**
- Mockup: `job_link_manager_mockup.html`, pubblicato come artifact "Job link manager – clickable mockup": https://claude.ai/artifact/QJqTp4SP3EpQhazJUjtasT
  - La copia nella sandbox (`/mnt/user-data/outputs/`) è temporanea; il codice va recuperato dall'artifact.
- Claude Doc "Two-Panel Job and Document Link Manager - Design Proposal": https://claude.ai/code/artifact/aa5c82c6-fdc2-4c5f-9f96-2f6d8b1b99e9
  - Sezioni: Overview, Layout, Data model, Preview, Handing over to the AI, Ideas for later, Suggested stack, Build order.
  - Contiene un commento aperto: pulsante "Generate" oppure solo pacchetto preparato?
  - La sezione Preview riporta ancora la conversione Word/Excel → PDF con LibreOffice, superata dalla decisione 7.3.

---

## 4. PRATICHE STUDIATE

Nessuna pratica è stata studiata davvero in questo progetto.

**Elenchi segnaposto del mockup** (inventati da Claude come esempio, da sostituire con quelli reali)

| Pratica | Documenti obbligatori | Documenti facoltativi |
|---|---|---|
| CIL | documento d'identità del cliente, visura catastale, planimetria catastale, titolo abilitativo o atto di provenienza, DURC dell'impresa | visura camerale dell'impresa, polizza RC dell'impresa |
| CFL | CIL depositata, dichiarazioni di conformità, relazione di fine lavori | foto del cantiere |

Per CIL e CFL (gli elenchi qui sopra non sono validati) e per CILA, SCIA e altre, tutto il resto è DA VERIFICARE:
- ordine e dipendenze: nessuno (unico indizio: la CFL presuppone la CIL depositata – DA VERIFICARE);
- documenti preparabili in parallelo: nessuno;
- chi produce ogni documento: nessuno;
- scadenze e validità, incluso il DURC: nessuno;
- riferimenti normativi e modulistica (Lombardia/comune): nessuno.

Riferimenti esterni a questo progetto
- La skill `crea-cfl` (progetto "Pratiche edilizie" / plugin) esiste già; il suo contenuto non è stato esaminato qui.
- Chat prevista "Pratiche · metodo CIL-CFL-SCIA" nel progetto Pratiche edilizie, con `dati_pratica.json` condiviso con `dati_cantiere.json`.

---

## 5. SCRIPT ESISTENTI

Il codice di questi script non è mai stato incollato in questo progetto. Va recuperato dal NAS.

| Script | Linguaggio | Cosa fa | Input → Output | Dove si trova |
|---|---|---|---|---|
| `seleziona_documenti.py` | Python | selezione dei documenti da copiare | proposta CSV → revisione in Excel → copia (es. in `Cantieri\<Cognome_Nome>\originali`) | `PSC_StudioFranco_pacchetto\02_script\00_raccolta\` |
| `converti_in_md.py` | Python | converte in Markdown con numeri di pagina, OCR opzionale | PDF / Word / Excel / p7m → .md | probabilmente `02_script\00_raccolta\` – DA VERIFICARE |
| `pulizia_settimanale.py` | Python | rapporto settimanale per la bacheca; idea: generare anche `rapporto.html` per il cruscotto | DA VERIFICARE | `Z:\Studio_AI\_organizzazione\` (sorgente in `06_organizzazione`) |
| builder dei documenti / script del pilota PSC | Python | generano i documenti del PSC; da generalizzare (README, sezione "Cosa generalizzare") | JSON → Word | `PSC_StudioFranco_pacchetto\02_script\` |

Codice prodotto qui: solo il mockup HTML (vedi sez. 3). Nessuno script backend è stato scritto.

---

## 6. MEMORIE / FILE .md

**`areas/link-web-server.md`** (alias: file link server, OpenMediaVault server, OMV)
- Vuole un web server usato solo da browser che raccoglie link ai file invece di copiarli, comprese cartelle di link.
- Server: vecchio i3, 8 GB, OpenMediaVault, con altri piccoli programmi Python già attivi; l'app va installata lì.
- App per le pratiche dell'architetto: pagina sempre a due pannelli, albero "vecchio stile" a sinistra (pochi file per cartella, per ultima modifica) con anteprima, area di lavoro della pratica a destra.
- Una nuova pratica (es. CIL) crea la cartella, le sottocartelle e la checklist; l'architetto la riempie inviando i link.
- Il pacchetto finale va a un'AI che estrae le informazioni e redige la documentazione.
- L'AI riceve le versioni Markdown, con il link al Word originale solo quando serve modificarlo.
- Conversione al momento del collegamento; ancora da capire se il risparmio di token vale e se la conversione rallenta.
- Mockup cliccabile pubblicato e documento di proposta di design creato.

**`areas/struttura-cartelle-studio.md`** (fonte: Cowork) – contenuto riportato nella sez. 2b.

**`index.md`** – solo il titolo "organizzazione studio".

**`RIEPILOGO_impostazione_2026-10-08.md`** (file di progetto) – riassunto:
- Architettura: Cowork = metodo; Claude Code = lavoro al PC; Hermes (GPT-6.1 Sol, Telegram, cron) = lavori quando Tony è via; script Python.
- Cartelle: vedi sez. 2a.
- Fatto: WSL2, Hermes, Claude Code, catena Hermes → Claude Code provata, pacchetto, script nuovi, bacheca, [Cantiere B] (379 file).
- Mancante: vedi sez. 9.
- Ritmo: riga in BACHECA a fine chat; rapporto il venerdì; pulizia il primo venerdì del mese.
- Idea cruscotto: `rapporto.html` servito dal NAS (Web Station, `python3 -m http.server` o Docker), oppure `hermes dashboard` sulla porta 9119.

**Istruzioni del progetto "Strumenti AI – Studio Franco"** (testo incollato in questa chat) – riassunto:
- Inizio chat: skill `organizza-studio`, lettura di BACHECA sezioni 1 e 3, proposta del nome chat (`Org · tema` / `Hermes · tema`).
- Fine chat: righe in BACHECA.
- Una casa per ogni cosa (tabella in CONVENZIONI.md).
- Script modificati solo da lì, provati prima su file di prova.
- Comandi Hermes verificati sulla documentazione ufficiale.
- Le cancellazioni le decide Tony.
- Nessun dato personale o economico dei clienti.
- Italiano semplice; un comando per riga, con indicato dove va dato.
- Elenco di 8 chat da aprire e dei progetti `PSC – Studio Franco` e `Pratiche edilizie`.

**Non disponibili qui** (contenuto DA VERIFICARE sul NAS): `CONVENZIONI.md`, `BACHECA.md`, `Guida_configurazione_Hermes.md`, `README.md` del pacchetto, `.hermes.md` / `CLAUDE.md`.

---

## 7. DECISIONI PRESE

1. **App sul server OMV esistente**, accanto agli script Python già attivi. Motivo: hardware sufficiente e file già lì.
2. **Interfaccia a due pannelli** (albero a sinistra, pratica con checklist a destra), con anteprima prima di collegare un file.
3. **Anteprima dei file Word/Excel**
   - 3.1 Niente conversione Word → PDF con LibreOffice solo per vedere il file. Motivo: lavoro e risorse in più quando il Markdown serve già per l'AI.
   - 3.2 Indirizzo emerso (proposto da Claude, che hai condiviso): Markdown come anteprima predefinita, docx-preview o mammoth.js per una vista più fedele, SheetJS per Excel, LibreOffice solo come eventuale pulsante "Exact view" futuro. Conferma definitiva: DA VERIFICARE.
4. **Conversione in Markdown al momento del collegamento** (idea tua):
   - l'AI legge il `.md`;
   - il Word originale viene passato solo se va modificato;
   - l'AI non sovrascrive mai l'originale, ma scrive una copia nella cartella della pratica.
5. **Archivio per CLIENTE**, date GG_MM_AA, lavori 110 % in archivio, cartelle personali di Nicola separate, scansione dell'HDD di Nicola prima di progettare la struttura.
6. **Link, non copie:** l'archivio è in sola lettura e l'AI scrive solo in `Z:\Studio_AI`.

---

## 8. IDEE SCARTATE

- **LibreOffice → PDF come anteprima predefinita.** Lento e pesante, e ridondante con il Markdown.
- **Viewer online di Microsoft o Google.** Richiedono che i documenti dei clienti siano raggiungibili da internet.
- **Symlink reali su disco** (sconsigliati da Claude, non discussi da te). Fragili su Windows e si rompono se il file si sposta. Scelti i link virtuali nel database.
- **Aprire una porta sul router per l'accesso esterno** (sconsigliato). Meglio una VPN.
- **Pulsante "Generate" che chiama l'API come primo passo** (sconsigliato all'inizio). Proposto di partire dal solo pacchetto preparato. Decisione aperta (sez. 9).

---

## 9. QUESTIONI APERTE

**App gestionale**
1. Elenchi reali dei documenti per CIL, CFL, CILA, SCIA: obbligatori/facoltativi, dipendenze, chi li produce, scadenze (DURC ecc.), normativa e modulistica di Regione Lombardia e comune.
2. Percorso della cartella che l'albero deve mostrare (es. `/srv/dev-disk-by-uuid-.../...`).
3. Installazione: Opzione A (venv + systemd) o B (Docker)?
4. Passo AI: pulsante "Generate" o solo pacchetto preparato? (commento aperto nel Claude Doc)
5. Test del risparmio di token: convertire 5 file reali con `converti_in_md.py` (documento scansionato, visura, relazione, foglio Excel) e confrontare token e qualità (circa 30 minuti).
   - Riferimenti trovati: circa −77 % di token per i PDF; risparmio probabilmente piccolo per Word, senza benchmark.
   - Tempi: Word in millisecondi; PDF con testo in meno di 1 secondo; scansioni con OCR alcuni secondi a pagina, più lente sull'i3 (stima).
6. Conversioni in background con stato sullo slot ("converting… / ready / needs OCR") e coda per i lavori lenti.
7. Provare docx-preview, mammoth.js e SheetJS sui documenti reali.
8. Aggiornare il mockup: conversione al collegamento, anteprima a due schede ("Original" / "What the AI reads"), manifest con `read`/`original`, nomenclatura italiana, elenchi reali.
9. Aggiornare la sezione Preview del Claude Doc, superata dalla decisione 7.3.
10. Allineare la nomenclatura delle cartelle pratica (sez. 2c) con CONVENZIONI.md e con le abitudini di Nicola.
11. Definire l'albero completo del server dopo la scansione dell'HDD di Nicola.

**Dal file RIEPILOGO – cosa manca, in ordine**
1. Creare i progetti claude.ai e caricare i file.
2. Attivare la bacheca e la regola in `.hermes.md`.
3. Disattivare il gateway di Hermes su Windows.
4. [Cantiere B]: Passo 2 Archivio → Controllo 1.
5. [Cantiere A]: rigenerare l'All. B, dichiarazione [Impresa A], archiviazione.
6. Generalizzare gli script del pilota.
7. Cron di Hermes del venerdì → Telegram.
8. Cruscotto nel browser sul NAS (chat `Org · cruscotto`; marca e modello del NAS DA VERIFICARE).