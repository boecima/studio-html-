> Testo fornito dall'utente il 10/10/2026. Nomi di clienti, cantieri e imprese, indirizzi e importi sostituiti da segnaposto perché il repository è pubblico; gli originali restano fuori da git.

# Riepilogo – Progetto Claude "[cantiere A] e .." (banco di prova metodo PSC – Studio Arch. Nicola Franco)
Periodo: 06/10/2026 – 08/10/2026 (date dei documenti del progetto). Riepilogo redatto il 10/10/2026.
Fonti: 5 documenti del progetto (Guida_PSC_multi-agente.md, Lezioni_metodo_PSC.md, Stato_PSC_[Cantiere A].md,
Riepilogo_organizzazione_studio.md, Progetto_Strumenti_AI_istruzioni.md) + chat "Alternatives to Hermes for
project assistance" (07/10/2026).
NOTA: questo progetto NON è il "gestionale file e pratiche". Le sezioni 3 e 4 sono in gran parte vuote per questo motivo.
Il materiale sul file manager e sulle pratiche è probabilmente in un altro progetto: DA VERIFICARE.

---

## 1. CONTESTO

- Obiettivo del progetto: mettere a punto un metodo per produrre PSC completi e la documentazione di sicurezza
  (D.Lgs. 81/08) senza CerTus, con agenti AI. Cantiere pilota: [Cantiere A] (capannone in acciaio a deposito agricolo,
  [indirizzo]), cartella `Z:\Antonio\PSC [Cantiere A]`.
- Obiettivo finale: guida generica + librerie riutilizzabili + skill "crea PSC", trasferite nel nuovo progetto
  "PSC – Studio Franco" (una chat e una cartella per cantiere).
- Obiettivo organizzativo (Riepilogo 08/10): ordinare strumenti, cartelle su `Z:\Studio_AI`, chat e progetti Claude,
  cruscotto, promemoria.
- Persone citate: Tony (operatore), Arch. Nicola Franco (CSP/CSE, decide e firma).
  "3 collaboratori": non citati in questo progetto – DA VERIFICARE.
- Problemi da risolvere emersi:
  - PSC di CerTus generico (schede standard, `$$$`, "gru a torre" invece di autogru, layout mancante, costi incompleti);
  - dati presenti nei file ma non letti (es. progettista strutture e collaudatore nell'istanza al Genio Civile);
  - incongruenze tra documenti (importo, data inizio, numero imprese);
  - file non catalogati: il registro fonti elenca solo i file che hanno prodotto un dato (chat 07/10);
  - ordine di cartelle, chat e progetti.

## 2. STRUTTURA NAS

Albero dei 3 collaboratori / gestionale: nessuno in questo progetto (DA VERIFICARE nell'altro progetto).
Strutture effettivamente definite qui:

### 2.1 Organizzazione generale (Riepilogo_organizzazione_studio, 08/10/2026)
~~~
Z:\Antonio\...  e  \\ADMINISTRATOR\Desktop\...     archivio dello studio – SOLA LETTURA per l'AI
Z:\Studio_AI\                                       unica cartella scritta dall'AI (in Ubuntu: /mnt/z/Studio_AI)
  .hermes.md = CLAUDE.md                            regole per Hermes e Claude Code (sempre identici)
  PSC_StudioFranco_pacchetto\                       libreria: 00 guida/lezioni/checklist · 01 librerie json · 02 script ·
                                                    03 modelli Word · 04 skill · 05 hermes · 06 organizzazione
  Cantieri\<Cognome_Nome>\originali | md | PSC_v2 | Stato_PSC_*.md
  Pratiche\<Tipo>_<Cognome>_<AAAA-MM>\
  _organizzazione\BACHECA.md · CONVENZIONI.md · pulizia_settimanale.py · rapporti\
~~~
- Copia d'origine del pacchetto: `Z:\Antonio\PSC [Cantiere A]\PSC_StudioFranco_pacchetto\` (da lì si copia in `Z:\Studio_AI`).
- In Ubuntu: NAS in `/mnt/z`, desktop di Nicola in `/mnt/nicola`.

### 2.2 Cartella di lavoro di un PSC (Guida, par. 2.4)
~~~
Z:\Antonio\PSC [Cantiere A]\PSC_v2\
  00_dati\        dati_cantiere.json, registro_fonti.md, lacune.md, ipotesi.md
  01_tempi\       cronoprogramma.json, relazione_tempi.md
  02_documenti\   01_PSC.docx, All_A, All_B, All_C, 04_Fascicolo
  03_grafica\     Layout_cantiere.dxf, tavole PDF, gantt.png
  04_modulistica\ 05…12 .docx
  05_verifica\    verifica_conformita.md
  PDF\            versioni finali per la firma
~~~
- La vecchia cartella `Documenti PSC (CerTus)` resta come riferimento e non va sovrascritta.

### 2.3 Regole di nomenclatura definite
- Cantieri: `Cantieri\<Cognome_Nome>\`
- Pratiche: `Pratiche\<Tipo>_<Cognome>_<AAAA-MM>\`
- Stato: `Stato_PSC_*.md`
- Chat del progetto Strumenti AI: `Org · tema` o `Hermes · tema` (anche `Script · …`)
- Chat del progetto Pratiche edilizie: `TIPO · Cognome`
- Chat PSC: es. `PSC · [Cantiere B] · Archivio`
- Moduli del CSP numerati 05–12
- Layer DXF del layout: `PSC_RECINZIONE`, `PSC_ACCESSI`, `PSC_VIABILITA`, `PSC_BARACCAMENTI`, `PSC_WC`, `PSC_DEPOSITI`,
  `PSC_RIFIUTI`, `PSC_QUADRO_ELETTRICO`, `PSC_AUTOGRU`, `PSC_LAVAGGIO_RUOTE`, `PSC_SEGNALETICA`, `PSC_EMERGENZA`
- Regola generale: "una sola casa per ogni cosa", la tabella in `CONVENZIONI.md` (contenuto non disponibile qui – DA VERIFICARE).

## 3. FILE MANAGER / MOCKUP

Nessuno. In questo progetto non c'è un file manager da browser né un mockup (pannelli, drag&drop, modalità copia/indice).
Idee vicine, ma diverse:
- "Cruscotto nel browser sul NAS" (Riepilogo, par. 6), allo stato di idea. Una pagina con bacheca, stato cantieri,
  scadenze e ultimo rapporto.
  - Strada semplice: `pulizia_settimanale.py` genera `rapporto.html`, pubblicato con `python3 -m http.server`
    o con il server web del NAS ("Web Station"), oppure con un container Docker che la rigenera ogni ora.
  - Strada più ricca: `hermes dashboard` (porta 9119) più la pagina del cruscotto.
  - Da decidere nella chat `Org · cruscotto`. Marca e modello del NAS: DA VERIFICARE.
- Indice centrale dei file (chat 07/10, mia proposta, non realizzata), descritto nella sezione 7.

## 4. PRATICHE STUDIATE

Nessuno studio completo (elenco documenti, dipendenze, chi produce cosa) è stato fatto qui. Esiste solo questo:

### CFL – Comunicazione di Fine Lavori
- Esiste la skill `crea-cfl`. Descrizione: prepara una CFL per lo studio Franco da una cartella pratica e dai moduli
  PDF editabili, con scheda dati, modulo, certificati e revisione incrociata.
- Elenco documenti, dipendenze, soggetti, normativa e modulistica regionale: DA VERIFICARE (nel contenuto della skill
  o nell'altro progetto).

### CIL (solo come dato del cantiere [Cantiere A])
- La CIL indica inizio lavori 30/10/2026 e una sola impresa ([Impresa A]). La notifica indica 30/11/2026 e 2 imprese.
  Decisione: inizio 30/11/2026, impresa unica [Impresa A].
- Allegati CIL trovati: `CIL…\Allegati\Visura Impresa.pdf`, `Durc Impresa.pdf`.
- Lacuna aperta L03 sulla CIL (contenuto della lacuna DA VERIFICARE in `lacune.md`).

### CILA, SCIA
- Nessuno studio. In programma la chat 8 `Pratiche · metodo CIL-CFL-SCIA` nel progetto "Pratiche edilizie", per
  costruire lo stesso schema di `crea-cfl`: `dati_pratica.json` condiviso con `dati_cantiere.json`, moduli, revisore.

### Documenti di sicurezza collegati (PSC, dal metodo)
- Ordine: Archivio → Fasi e Tempi → in parallelo Rischi (All. B), Costi (All. C), Fascicolo (All. XVI) e Grafica
  (All. A Gantt + layout) → Relazione PSC → Modulistica → Revisore → stampa, firma, consegna.
- Controlli umani: dopo l'Archivio e dopo il cronoprogramma.
- Producono: agenti AI. Verifica e firma: CSP (Nicola).
- Moduli 05–12: 05 designazione CSP/CSE; 06 richiesta ITP (impresa affidataria e subappaltatori, con patente a crediti,
  DURC, organico medio); 07 trasmissione PSC (art. 101); 08 verbale consegna PSC al committente; 09 verifica idoneità
  POS (All. XV p. 3.2); 10 riunione di coordinamento; 11 sopralluogo CSE; 12 ordine di servizio, sospensione,
  segnalazione inadempienze (art. 92 c. 1 lett. e–f).
- Scadenze e validità: DURC [Impresa A] scade il 29/10/2026, prima dell'inizio lavori, e va rinnovato (D5).
  La notifica preliminare va aggiornata se cambiano importo, date o imprese.
- Riferimenti normativi citati: D.Lgs. 81/08 – All. XV (p. 2.1.2 a–l, 2.2.1, 2.2.2 a–n, 2.2.3, 3.2, 4.1 a–g, 4.1.3),
  All. XVI, art. 27 (patente a crediti), art. 91 c. 2-bis (ordigni bellici), art. 92 c. 1 lett. b ed e–f, art. 101;
  Prezzario Regione Campania (CAM26 da riscontrare).

## 5. SCRIPT ESISTENTI

Il codice degli script non è in questo progetto, quindi non posso riportarlo. Le posizioni sono quelle dichiarate nel
Riepilogo; i contenuti sono DA VERIFICARE nella cartella del pacchetto.

| Script | Linguaggio | Cosa fa (come descritto) | Input / Output | Posizione |
|---|---|---|---|---|
| `seleziona_documenti.py` | Python | Selezione documenti: proposta CSV → revisione in Excel → copia dei selezionati | cartella sorgente (es. desktop di Nicola) → CSV/Excel di proposta, file copiati in `originali\` | `02_script/00_raccolta/` |
| `converti_in_md.py` | Python | Converte PDF/Word/Excel/p7m in Markdown con numeri di pagina, OCR opzionale | file in `originali\` → file `.md` (cartella `md\`) | `02_script/00_raccolta/` (DA VERIFICARE) |
| `pulizia_settimanale.py` | Python | Pulizia e rapporto settimanale; in futuro anche `rapporto.html` e cron Hermes del venerdì su Telegram | bacheca/cartelle → rapporto in `rapporti\` | `Z:\Studio_AI\_organizzazione\` (e `06_organizzazione` del pacchetto) |
| Builder dei documenti del pilota (PSC, allegati, moduli, Gantt, layout DXF) | Python (python-docx, openpyxl, ezdxf, matplotlib, pandas) | Rigenerano i documenti dai JSON | JSON di `00_dati` / `01_tempi` → docx, xlsx, dxf, png | `PSC_StudioFranco_pacchetto\02_script` |

- Limite noto dei builder: percorsi assoluti (`/home/claude/work/out`) e testi di copertina scritti a mano.
  Vanno generalizzati (percorsi relativi a `PSC_v2`, testi da `dati_cantiere.json`). Vedi README, "Cosa generalizzare".
- Prova [Cantiere B]: 379 file letti dal desktop di Nicola, selezione per cartella, copia in `originali\`;
  conversione md in corso all'08/10.

## 6. MEMORIE / FILE .md

### Documenti del progetto (contenuto disponibile)
1. `Guida_PSC_multi-agente.md` (06/10/2026). Parte 1: verifica dei documenti CerTus e lacune. Parte 2: principi (un solo
   `dati_cantiere.json`, niente `$$$`, fonte per ogni dato, file e non chat, due controlli umani), 10 agenti, ordine di
   esecuzione, struttura delle cartelle. Parte 3: compiti dettagliati dei Passi 1–8. Parte 4: consigli pratici.
2. `Lezioni_metodo_PSC.md`: registro delle correzioni al metodo (data – passo – problema – regola). Righe: lettura di
   tutti i file; mezzi dal cantiere reale; ordigni bellici sempre valutati; costi su tutte le lettere a–g; patente a
   crediti nella richiesta ITP; layout obbligatorio; confronto P80 / notifica (D7-bis); impaginazione ibrida come
   standard; costi su tre livelli; rigenerare tutti i documenti quando cambia un dato condiviso; indice verificato sul
   PDF; script con percorsi relativi [da fare]; ordine di chiusura JSON → documenti → PDF.
3. `Stato_PSC_[Cantiere A].md` (07/10): passi completati, decisioni di Nicola, cose rimaste del Passo 8, passaggio al
   pacchetto `PSC_StudioFranco_pacchetto` (64 file).
4. `Riepilogo_organizzazione_studio.md` (08/10): architettura degli strumenti, cartelle, fatto / da fare, ritmo,
   idea cruscotto.
5. `Progetto_Strumenti_AI_istruzioni.md`: istruzioni del progetto "Strumenti AI – Studio Franco", 8 chat iniziali,
   cenni ai progetti "PSC – Studio Franco" e "Pratiche edilizie".

### File citati ma non disponibili qui (contenuto DA VERIFICARE)
`BACHECA.md`, `CONVENZIONI.md`, `.hermes.md` / `CLAUDE.md`, `SOUL.md`, `Guida_configurazione_Hermes.md`, `README.md`
del pacchetto, `Istruzioni_progetto_PSC_Studio_Franco.md`, `Guida_PSC_generica`, `Checklist_revisore`; e per il
cantiere: `registro_fonti.md` (46 fonti), `lacune.md` (30), `ipotesi.md`, `relazione_tempi.md`,
`verifica_conformita.md`, `verifica_costi_scenarioB.md`.

### Memoria di Claude
Nessun file di memoria salvato.

## 7. DECISIONI PRESE

### Organizzazione (confermate nei documenti)
- `Z:\Studio_AI` è l'unica cartella scritta dall'AI; l'archivio dello studio è in sola lettura. Motivo: non toccare
  mai gli originali.
- Ruoli: Cowork per il metodo; Claude Code per il lavoro al PC; Hermes per i lavori quando Tony non c'è (Telegram,
  cron); script Python senza costi.
- Un solo gateway Hermes acceso (conflitto Telegram tra Windows e Ubuntu).
- `.hermes.md` e `CLAUDE.md` sempre identici.
- Le cancellazioni le decide Tony; nessun dato personale o economico dei clienti nelle chat di Strumenti AI.
- Ritmo: riga in BACHECA a fine chat; venerdì 10 minuti di rapporto; primo venerdì del mese, pulizia di 30 minuti.

### Metodo PSC
- Fonte unica `dati_cantiere.json`; ipotesi dichiarate in `ipotesi.md`; fonte (file e pagina) per ogni dato.
- Impaginazione ibrida come standard dello studio.
- Ordine di chiusura: JSON e ipotesi → documenti → PDF.

### Cantiere [Cantiere A] (decisioni di Nicola)
D1 importo [importo] €; D2 inizio 30/11/2026; D3 impresa unica [Impresa A]; D4 autogru; D5 DURC da rinnovare;
D6 accesso da progetto; D7 notifica da aggiornare; D7-bis notifica a 300 gg (fine 26/09/2027); costi scenario B
([importo] €, 2,50 %); impaginazione ibrida.

### Gestione file (chat 07/10 – PROPOSTE di Claude, non decisioni confermate da Tony)
- Indice centrale fuori dalle cartelle dei documenti (es. `PSC_v2\00_dati\indice_file.sqlite`), con hash SHA-256,
  percorso, tipo di documento, dati estratti. Nato dalla richiesta di Tony di non avere JSON accanto ai PDF.
- Classificazione a strati: regole su nome ed estensione → NuExtract per i casi ambigui → controllo umano
  (cartella `da_rivedere`), con prova sulla cartella [Cantiere A].
- Priorità suggerite: Git subito; Paperless-ngx per la catalogazione; Docling per le tabelle di computo e prezzario.
- Se siano state adottate: DA VERIFICARE.

## 8. IDEE SCARTATE

- Metadati scritti dentro i PDF originali: sconsigliato. Cambia l'hash, può invalidare la firma digitale e viola la
  regola sugli originali. (Proposta di Claude, 07/10)
- NTFS Alternate Data Streams (`file.pdf:meta.json`): da evitare, si perdono con email, zip, cloud e NAS. (Proposta di
  Claude, 07/10)
- JSON accanto ai PDF nella stessa cartella: escluso da Tony ("dont want to have a folder with pdf and json together").
- RAG per singolo cantiere: giudicato marginale. Meglio JSON + registro fonti + ricerca full-text; RAG solo per la
  libreria normativa trasversale, se cresce. (Valutazione di Claude, 07/10)
- n8n / Make come base del flusso: secondari, da valutare solo dopo che il flusso principale è stabile (es. promemoria
  DURC, smistamento file).
- Imparare molti framework di agenti insieme: sconsigliato; meglio Python, il pattern skill+JSON, MCP e Claude Code.
- Cantiere [Cantiere A]: "gru a torre" sostituita da autogru; costi [importo] € (13,14 %) superati da [importo] €;
  impaginazioni "metodo" (44 pp.) e "CerTus" (112 pp.) tenute solo come varianti; computo xlsx del 17/12/25 scartato
  (vecchio e danneggiato), usato il PDF del 13/03/26.

## 9. QUESTIONI APERTE

### Gestionale / organizzazione
- Dove si trovano il mockup del file manager, la struttura NAS per i collaboratori e lo studio delle pratiche: DA
  VERIFICARE (altro progetto o altra chat).
- Marca e modello del NAS; scelta della strada per il cruscotto.
- Contenuto di `CONVENZIONI.md` e `BACHECA.md` da includere nel repository.
- Indice file con hash / Paperless-ngx / NuExtract: solo proposti, da decidere e provare.
- Git per gli script e i JSON: suggerito, non risulta attivato.
- Da fare dal Riepilogo: creare i progetti `PSC – Studio Franco`, `Pratiche edilizie` e `Strumenti AI`; attivare la
  bacheca e la regola in `.hermes.md`; disattivare il gateway Hermes su Windows; [Cantiere B] Passo 2 e Controllo 1;
  generalizzare gli script prima del terzo cantiere; cron Hermes del venerdì.
- Metodo CIL/CILA/SCIA da costruire partendo da `crea-cfl` (chat 8).

### Cantiere [Cantiere A] (Passo 8)
1. Rigenerare l'All. B dopo il cambio dei costi (tre frasi non allineate).
2. Lettere e–g a zero: dichiarazione [Impresa A] di mezzi e personale propri, oppure importo simbolico per f e g.
3. Confermare o correggere ogni riga di `ipotesi.md` e del PSC §13.
4. Riscontrare le analisi prezzi sul Prezzario CAM26.
5. Lacune: CIL (L03), recapiti collaudatore (L09), patente a crediti / DURC / matricole [Impresa A], progetto linee vita
   (IPF02), rilievo viabilità (L24), amianto rudere (IPR02).
6. Aggiornare la notifica preliminare; firma digitale dei PDF; trasmissione con il modulo 07; archiviare il progetto.