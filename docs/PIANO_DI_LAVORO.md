# Piano di lavoro — Gestionale file e pratiche dello studio

Stato: aggiornato il 10/10/2026 sera. Fatto: esempio funzionante (app/), 12 schede di ricerca (docs/pratiche/), 12 JSON generati (pratiche/). Tutto quello che c'è nei riepiloghi (`docs/riepiloghi/`) vale come linea guida, non come decisione presa.

## Quadro

- **Dove lavoriamo:** Campania, soprattutto province di Avellino, Benevento, Napoli e Caserta. La modulistica cambia per comune, quindi ogni flusso va controllato sui comuni dove lo studio lavora davvero.
- **Cosa produce il sistema, per ogni pratica (2 o 3 uscite):**
  1. **Indice** — un file `pratica.json` + `INDICE.md` che dice dove sta ogni documento (percorso originale, data, impronta del file). È la base per tutto il resto. Sempre prodotto.
  2. **Copia** — i file copiati nella cartella della pratica con il nome standard, pronti da inviare. A scelta.
  3. **Pacchetto per l'AI** — le versioni Markdown dei documenti + un `manifest.json`, per far compilare il modulo (CFL, CIL, …) all'AI. A scelta.
- **Interfaccia:** pagina a due pannelli. Sinistra: albero dell'archivio vecchio stile, solo file di ufficio. Destra: la pratica, con gli slot dei documenti in ordine (chi viene prima, chi va in parallelo). Più poche funzioni cliccabili utili: cartella **Inviati** (cosa è già partito dallo studio), scheda **Indice cliccabile**, e altro da decidere.

## Dove siamo (10/10/2026)

- **Fase 1 — fatta la prima passata.** 12 schede in `docs/pratiche/` (CFL, SCA, CIL, CILA+CILAS, SCIA, PdC, catasto, sismica, sanatoria, paesaggistica, energia) e i JSON generati da `pratiche/da_scheda.py`. Limite: dall'ambiente cloud i siti ufficiali (normattiva, Regione, Agenzia Entrate, comuni) erano bloccati, quindi le schede nascono da riassunti di ricerca e ogni dato non letto alla fonte è marcato "DA VERIFICARE". Prossimo passo: riaprire le fonti (da Cowork o da un ambiente con rete aperta) e togliere i "DA VERIFICARE", poi far correggere le schede a Franco e Nicola.
- **Fase 3 — esempio funzionante.** `app/server.py` + pagina a due pannelli, 3 uscite, scheda Inviati, scheda Indice cliccabile, archivio di prova. Manca: anteprima Word/Excel via Markdown, conversione automatica nel pacchetto AI, installazione sul NAS come servizio.
- **Fase 2 e 4 — non iniziate.**

## Fasi, in ordine di importanza

### Fase 1 — Flussi delle pratiche (la cosa più importante)

Obiettivo: per ogni tipo di pratica, un file descrittivo unico (`pratiche/<tipo>.json`) che l'app legge per costruire slot, ordine e infografica. Niente disegni a mano.

Per ogni documento del flusso:
- codice e nome (es. `CFL-03 Dichiarazione conformità impianti`)
- obbligatorio / facoltativo / dipende dal caso (es. solo se ci sono impianti)
- **prerequisiti** → l'ordine
- **gruppo parallelo** → cosa si può fare insieme
- chi lo produce: tecnico, cliente, impresa, ente
- validità (es. DURC 120 giorni) → avvisi di scadenza
- nome file standard e sottocartella di destinazione
- riferimento normativo e modulo (regionale / comunale)

Lavoro:
1. **Ricerca per pratica, per le 4 province.** Fonti: modulistica unificata Regione Campania, SUE/SUAP dei comuni principali (Avellino, Benevento, Napoli, Caserta e i comuni dove lo studio lavora, da elencare), dPR 380/2001, Regolamento Edilizio Tipo. Per ogni pratica: una scheda `docs/pratiche/<tipo>.md` con elenco documenti, ordine, differenze comunali trovate, link ai moduli. Segnare "DA VERIFICARE" dove la fonte non è chiara.
2. **Ordine delle pratiche da studiare:** CFL → CIL → CILA → SCIA / SCIA alternativa → SCA (agibilità) → PdC → DOCFA/catastali → sanatoria/condono → paesaggistica → deposito sismico (Genio Civile) → APE / Legge 10 → varianti e cambi d'uso → altro dall'elenco del riepilogo 1.
3. **Dalla scheda al file JSON** + un disegno di prova dell'infografica per la CFL, da far correggere a Franco e Nicola.
4. **Validazione sul caso reale:** il pacchetto CFL di [Cliente A] (riepilogo 1) e la CIL del cantiere [Cantiere A] (riepilogo 3) sono i casi di prova.

Uscita della fase: `docs/pratiche/*.md`, `pratiche/*.json`, un'infografica per pratica.

### Fase 2 — Struttura del NAS e nomenclatura

Tre strutture esistono già (riepilogo 1: V1, Proposta A, V2 per tipo; riepilogo 4: per cliente, date GG_MM_AA). Vanno unificate in una sola.

1. Tabella di confronto delle tre strutture, con pro e contro.
2. Decidere con Nicola: archivio per cliente (confermato il 09/10) → lavoro → pratiche; numerazione; formato data nei nomi (GG_MM_AA, abitudine di Nicola, contro AAAA-MM-GG, che ordina da sola); cosa fare di `99_CHIUSE`.
3. Aggiornare `struttura.py` di conseguenza e scrivere `CONVENZIONI.md` definitivo.
4. Formare i collaboratori: una pagina, le regole in 10 righe.

### Fase 3 — Applicazione web

Base: il mockup "Job link manager" (riepilogo 4, artifact `QJqTp4SP3EpQhazJUjtasT`) e lo schema a 4 tabelle (tipi, documenti richiesti, pratiche, file collegati).

1. Recuperare il codice del mockup e portarlo nel repository (`app/`).
2. Scegliere l'installazione sul NAS OMV: servizio systemd con venv (semplice) oppure Docker. Proposta: systemd, perché gli altri script Python girano già così.
3. Backend minimo: Python + FastAPI + SQLite. L'archivio in sola lettura; l'app scrive solo nelle cartelle delle pratiche e in `Z:\Studio_AI`.
4. Pannello sinistro: albero con caricamento a richiesta, solo estensioni di ufficio, anteprima PDF/immagini; Word ed Excel via Markdown (decisione 7.3 del riepilogo 4).
5. Pannello destro: la pratica costruita dal JSON della fase 1. Slot bloccati finché i prerequisiti non sono soddisfatti, gruppi paralleli affiancati, barra di avanzamento.
6. Le 3 uscite: indice (sempre), copia, pacchetto AI.
7. **Inviati:** ogni invio (PEC, portale, sportello) registra data, canale, protocollo e i file inviati; i file inviati diventano immutabili (già `99_Emessi` / `99_TRASMESSI` nelle strutture). La scheda mostra cosa è partito e cosa manca.
8. Funzioni di contorno: avvisi scadenze (DURC), registro chi-ha-collegato-cosa, controllo notturno dei file spostati.

### Fase 4 — Indice cliccabile

Dato di partenza: l'indice per parole (`indice.py`, FTS5) funzionava ma nessuno lo usava. Idea: ricerca senza tastiera, solo clic: cliente → pratica → tipo di file → risultato.

1. **Ricerca breve** (prima di costruire): come fanno gli strumenti che la gente usa davvero (filtri a faccette, navigazione per categoria, "ultimi aperti", ricerca per esempio). Uscita: una pagina di note con 2–3 soluzioni e una raccomandazione.
2. Prototipo nella scheda Indice dell'app, alimentato dal `pratica.json` di ogni pratica + metadati dei file.
3. Prova con Nicola per una settimana, poi si decide.

### Fase 5 — Compilazione con l'AI

1. Partire dalla skill `crea-cfl` esistente e dal pacchetto AI della fase 3.
2. `dati_pratica.json` condiviso con `dati_cantiere.json` del metodo PSC.
3. Prima la CFL, poi la CIL; il pulsante "Genera" viene dopo il pacchetto preparato (questione aperta del riepilogo 4).

## Calendario proposto

| Settimana | Lavoro |
|---|---|
| 1–2 | Fase 1: ricerca CFL, CIL, CILA, SCIA per le 4 province; schede `.md`; JSON e infografica della CFL |
| 3 | Fase 1: SCA, PdC, catastali; Fase 2: tabella di confronto strutture e decisione con Nicola |
| 4 | Fase 2: `struttura.py` aggiornato, `CONVENZIONI.md`; Fase 3: codice del mockup nel repo, scelta installazione |
| 5–6 | Fase 3: albero + anteprima + pratica dal JSON; uscita "indice" |
| 7 | Fase 3: copia, pacchetto AI, Inviati |
| 8 | Fase 4: ricerca sull'indice cliccabile e prototipo |
| 9+ | Fase 5: CFL compilata dall'AI sul caso reale; poi le altre pratiche |

Le settimane sono una stima con poche ore a settimana. L'ordine conta più delle date.

## Da decidere (prima o poi, non ora)

- Region/comuni: elenco dei comuni dove lo studio lavora di più, per controllare la modulistica locale.
- Struttura NAS unica (fase 2).
- systemd o Docker sul NAS.
- Repository pubblico o privato: finché è pubblico, niente nomi di clienti, importi, indirizzi, token (vedi `.gitignore`).
- Il significato delle sigle dello studio DNL, ASID, CIR.

## Cosa c'è nel repository

```
docs/
  PIANO_DI_LAVORO.md      questo file
  riepiloghi/             i riepiloghi dei progetti Claude precedenti (nomi mascherati)
  pratiche/               (fase 1) una scheda per pratica
pratiche/                 (fase 1) i file JSON letti dall'app
app/                      (fase 3) l'applicazione web
```
