# Riepilogo progetto "mappe catastali"
Chat: "Querying multiple parcels from Zornade cadastral API"
Ultimo aggiornamento: ~1 ottobre 2026
NOTA: questo progetto NON contiene il lavoro sul "gestionale file e pratiche" (NAS, file manager, pratiche edilizie).

> Testo incollato dall'utente il 10/10/2026. Unica modifica: i nomi dei proprietari negli esempi sono sostituiti da segnaposto ([Proprietario A] ecc.) perché il repository è pubblico.

## 1. CONTESTO
- Obiettivo: cercare più particelle catastali alla volta (comune / foglio / particella) tramite l'API di Zornade (https://app.zornade.com/api, token "lettura particelle"), vederle su mappa e generare un file da aprire in forMaps.
- Uso in ufficio: la pagina può essere usata anche da altri PC della stessa rete (modalità `rete`).
- Problemi affrontati: particelle non trovate (es. Pannarano fg. 8, 1038 e 1039, presenti su forMaps), sfondo mappa bloccato, file .fmaps che non si apriva, poligoni assenti in forMaps.
- Utenti / 3 collaboratori dello studio: nessuno (non discusso in questo progetto).

## 2. STRUTTURA NAS
nessuno

## 3. FILE MANAGER / MOCKUP
nessuno (nessun file manager). L'unica interfaccia esistente è la pagina web locale di cerca_particelle.py (vedi sezione 5).

## 4. PRATICHE STUDIATE
nessuno

## 5. SCRIPT ESISTENTI

### cerca-particelle.html (prima versione, poi superata)
- Linguaggio: HTML/JS con Leaflet
- Cosa fa: strumento locale per cercare più particelle tramite l'API Zornade
- Stato: sostituito da cerca_particelle.py (DA VERIFICARE se ancora in uso)

### cerca_particelle.py (versione attuale)
- Linguaggio: Python 3, solo libreria standard (`requests` sostituito con `urllib`, nessun `pip install` necessario)
- Posizione: `E:\Particelle` (in un messaggio successivo compare anche `C:\pyton pro\particelle`: DA VERIFICARE quale sia quella attuale)
- Avvio:
  - `python cerca_particelle.py particelle.txt` → modalità a riga di comando
  - `python cerca_particelle.py` → apre la pagina web locale (http://127.0.0.1:8765)
  - `python cerca_particelle.py rete` → pagina raggiungibile da altri PC della stessa rete (serve il permesso del firewall di Windows su "Reti private"; una sola ricerca alla volta; il PC che la ospita deve restare acceso con la finestra aperta)
- Input:
  - file `particelle.txt` con righe `Comune;foglio;particella` (es. `Pannarano;8;285`), oppure coordinate `lat,lng` (es. `40.995181,14.700040`); si possono mescolare comuni diversi
  - dalla pagina web: comune, proprietari (nome + colore), per ogni proprietario uno o più fogli con particelle separate da virgola; per ogni foglio un "Colore foglio" (default "Come proprietario")
  - colori disponibili: Rosso, Blu, Verde, Arancione, Viola, Giallo, Grigio, Nero
- Logica di ricerca (endpoint Zornade `/parcels/search`, `/parcels/locate`, dettaglio particella):
  1. prova grafie diverse del foglio (`8`, `08`, `0008`) e del comune
  2. scorre tutte le pagine dei risultati
  3. se manca ancora, scansiona la zona sulla mappa (1-3 minuti)
  4. se più particelle hanno lo stesso numero nel comune, verifica il foglio dai dettagli della particella
- Output:
  - CSV dei risultati (se è aperto in Excel salva come `risultati_HHMMSS.csv` invece di andare in errore)
  - file forMaps `.fmaps`: marker con Etichetta `Fg.8/Pt.285`, Denominazione `PANNARANO - Foglio 8 - Particella 285`, Note con m², zona sismica, OMI €/m², proprietario; sfondo Google Streets, zoom 17, layer particelle/fabbricati/numeri attivi; contorni disegnati (DrawnItems) colorati
  - `mappa.html`: anteprima Leaflet con contorni colorati, legenda per proprietario (e "Nome - Fg. X" per i fogli con colore proprio), mappa catastale ufficiale dell'Agenzia delle Entrate (WMS, visibile solo con zoom ravvicinato), scelta Mappa/Satellite
  - nomi dei file dalla pagina web: `[Proprietario A].fmaps`, `[Proprietario A] - mappa.html`, `[Proprietario A].csv`; con più proprietari `[Proprietario B] - [Proprietario C].fmaps`; con ricerche ripetute `(2)`, `(3)`, ... senza sovrascrivere; senza proprietario prende il nome del comune
- Codice completo: NON riportabile qui. Scaricare l'ultima versione di `cerca_particelle.py` dall'ultima scheda file della chat.

## 6. MEMORIE / FILE .md
nessuno

## 7. DECISIONI PRESE
- Passaggio da HTML a script Python con pagina web locale, per superare i limiti del browser e salvare i file su disco.
- Solo libreria standard Python, per evitare problemi di installazione di `requests`.
- Formato .fmaps copiato da un file salvato dall'utente in forMaps; Denominazione e Ricerche scritte esattamente come forMaps (causa probabile del file che non si apriva).
- Sfondo OpenStreetMap sostituito (bloccato sui file locali); aggiunto il WMS catastale dell'Agenzia delle Entrate.
- File nominati per proprietario e mai sovrascritti.
- Colore per proprietario, con possibilità di colore diverso per singolo foglio.

## 8. IDEE SCARTATE
- Riparare la libreria `requests` sul PC: scartato, sostituita con `urllib`.
- Mettere m² e proprietario nel campo di ricerca di forMaps: scartato perché probabilmente impediva l'apertura del file; spostati in Etichetta/Note.
- Accesso dall'esterno della rete (casa ↔ ufficio): non implementato, servirebbe una VPN.

## 9. QUESTIONI APERTE
- Particelle 1038 e 1039 (Pannarano fg. 8): Zornade potrebbe avere dati più vecchi di forMaps. DA VERIFICARE se ora vengono trovate.
- Poligoni in forMaps: era stato chiesto all'utente un file .fmaps con un poligono disegnato a mano come campione; i test successivi includono i contorni colorati. DA VERIFICARE se si aprono correttamente in forMaps.
- Apertura del .fmaps dopo la correzione del formato: DA VERIFICARE.
- Cartella di lavoro: `E:\Particelle` o `C:\pyton pro\particelle`. DA VERIFICARE.
- Il token API Zornade è scritto in chiaro nella chat: NON metterlo nel repository (usare una variabile d'ambiente o un file escluso con .gitignore) e valutare di rigenerarlo.
