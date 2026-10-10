# Gestionale file e pratiche dello studio

Pagina web a due pannelli per uno studio di architettura in Campania: a sinistra l'archivio (sola lettura), a destra la pratica con la lista dei documenti in ordine. Si trascina un file nello slot giusto; la pratica produce un indice, una copia ordinata dei file e un pacchetto per l'AI che compila il modulo.

Solo Python 3 standard: niente da installare.

## Provare in 2 minuti

```
python esempio/crea_esempio.py            # archivio finto con PDF veri (nessun dato reale)
copy app\config.esempio.json app\config.json      (Windows)   /   cp app/config.esempio.json app/config.json
python app/server.py                      # poi apri http://127.0.0.1:8780
python app/server.py rete                 # raggiungibile dagli altri PC dello studio
```

Sul NAS: in `app/config.json` scrivi il percorso dell'archivio (es. `\\\\192.168.1.9\\Nas\\01_CLIENTI` o `/srv/dev-disk-by-uuid-…/Nas`) e la cartella dove creare le pratiche.

## Cosa fa

| Scheda | Cosa c'è |
|---|---|
| **Pratica** | i documenti del tipo scelto, a passi: un documento tratteggiato è bloccato finché mancano i suoi prerequisiti; quelli dello stesso passo si preparano in parallelo. Avviso se un DURC o una visura sono più vecchi della loro validità. |
| **Inviati** | ogni invio (PEC, portale, sportello) con data, protocollo e i file partiti, copiati in sola lettura in `99_TRASMESSI/`. Sotto: cosa è collegato ma non ancora inviato. |
| **Indice** | ricerca senza tastiera: clicchi cliente → pratica → documento → formato. Mostra dove sta il file e apre la cartella. |

Le tre uscite di una pratica:

1. **Indice** (sempre): `pratica.json` + `INDICE.md` nella cartella della pratica. Dicono dove sta ogni file nell'archivio, con data e impronta SHA-256. L'archivio non viene toccato.
2. **Copia**: i file collegati copiati nelle sottocartelle della pratica con nome standard `AAAA-MM-GG_CODICE_Descrizione.ext`.
3. **Pacchetto per l'AI**: `manifest.json` con l'elenco dei documenti, le fonti e i controlli incrociati; i PDF/Word vanno convertiti in Markdown con `converti_in_md.py` (dal pacchetto PSC).

## Dove sono le regole

- `pratiche/*.json` — un file per tipo di pratica (CFL, CIL, …). Ogni documento ha codice, obbligatorietà, prerequisiti, gruppo parallelo, chi lo produce, validità, parole chiave per il suggerimento automatico, sottocartella. L'app legge questi file: per cambiare una lista si modifica il JSON, non il codice.
- `docs/pratiche/*.md` — le schede di ricerca per ogni pratica (norme, modulistica dei comuni campani, tempi, fonti). I JSON vanno allineati alle schede.
- `docs/PIANO_DI_LAVORO.md` — il piano.
- `docs/riepiloghi/` — quello che è stato fatto nei progetti Claude precedenti.

## Regole di sicurezza del programma

- L'archivio è in sola lettura: il server non scrive e non cancella mai lì.
- Si scrive solo nella cartella delle pratiche.
- I percorsi richiesti dal browser non possono uscire dall'archivio o dalla pratica.
- Quello che è stato inviato diventa a sola lettura.
- Non si scollega un documento se un altro, già collegato, dipende da lui.
