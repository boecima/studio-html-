# ENE — APE (Attestato di Prestazione Energetica) e relazione tecnica "ex Legge 10" (art. 8 D.Lgs. 192/2005)

Regione: Campania · Province: Avellino, Benevento, Caserta, Napoli (Salerno solo se diversa) · Data ricerca: 2026-10-10
Stato della scheda: bozza da verificare con il tecnico. Ogni riga con fonte; quello che non si trova è "DA VERIFICARE".
Nota di metodo: normattiva.it, apecampania.enea.it e i siti comunali non erano raggiungibili in sessione (accesso di rete bloccato); le informazioni sul portale regionale derivano da articoli di settore e dalla nota regionale agli Ordini. I punti non letti direttamente sono "DA VERIFICARE".

## 1. Cos'è e quando si usa
L'APE (art. 6 D.Lgs. 192/2005; DM 26/6/2015 "Linee guida APE") attesta la classe energetica di un edificio o unità immobiliare. È obbligatorio: per nuove costruzioni e ristrutturazioni importanti (a cura del costruttore, da allegare alla segnalazione di agibilità); per vendita, trasferimento a titolo oneroso o gratuito e nuova locazione (a cura del proprietario, con clausola nel contratto e allegazione, tranne locazione di singole unità); negli annunci commerciali (indice e classe); per edifici pubblici aperti al pubblico > 250 mq; vale 10 anni, purché siano rispettati i controlli periodici degli impianti (dPR 74/2013), altrimenti decade al 31/12 dell'anno successivo alla prima scadenza non rispettata; va rifatto dopo interventi che cambiano la classe [F1][F2][F3]. In Campania il certificatore (requisiti dPR 75/2013) trasmette l'APE in XML v5 al catasto regionale "APE-Campania" (portale ENEA, attivo dal 7/1/2025, ha sostituito il SID; integrato con il SIAPE nazionale) e consegna al committente l'APE con la ricevuta del portale entro 15 gg [F4][F5][F6].
La relazione tecnica "ex Legge 10" (art. 8 c. 1 D.Lgs. 192/2005; schemi del DM 26/6/2015 "relazione tecnica", allegati 1-2-3) dimostra il rispetto dei requisiti minimi (DM 26/6/2015 "requisiti minimi", aggiornato dal DM 28/10/2025 in GU 5/12/2025 con efficacia dopo 180 gg — DA VERIFICARE) per nuove costruzioni, ristrutturazioni importanti di 1° e 2° livello, riqualificazioni energetiche e sostituzione di impianti; è firmata dal progettista e depositata al Comune (SUE) con il titolo edilizio, prima dell'inizio lavori; a fine lavori il direttore dei lavori assevera la conformità al progetto e alla relazione e presenta l'APE con la fine lavori (art. 8 c. 2) [F7][F8].
Quando NON si usano: APE non dovuto per fabbricati isolati < 50 mq utili, edifici industriali/artigianali/agricoli non climatizzati, ruderi e immobili al grezzo (con dichiarazione in atto), box/cantine/depositi (art. 3 c. 3) [F1][F9]; relazione ex L. 10 non dovuta per interventi senza rilevanza energetica (opere interne senza impianti/involucro, manutenzione ordinaria) — in questi casi il tecnico dichiara nel titolo che l'intervento non rientra nel campo del D.Lgs. 192/2005. L'APE non sostituisce il libretto d'impianto (DM 10/2/2014) né il rapporto di controllo efficienza energetica.

## 2. Chi è coinvolto
| Soggetto | Ruolo | Cosa produce |
|---|---|---|
| committente (proprietario / costruttore / locatore) | obbligato a dotare l'immobile di APE e a depositare la relazione ex L. 10 (tramite il tecnico) | incarico, dati catastali, titoli, libretto impianto, bollette, documentazione impianti |
| certificatore energetico (dPR 75/2013: laurea/diploma tecnico + abilitazione + iscrizione albo, oppure corso regionale; indipendenza dichiarata ex artt. 359 e 481 c.p.; non deve aver progettato/diretto l'opera né avere parentela entro il 4° grado) | sopralluogo obbligatorio, calcolo (UNI/TS 11300, software certificato CTI), firma APE, trasmissione al catasto regionale | APE (PDF firmato + XML v5), ricevuta APE-Campania, dichiarazione di indipendenza |
| progettista termotecnico (iscritto all'albo) | relazione ex L. 10 con verifica requisiti minimi; sanzione 30% parcella se omessa/non conforme (art. 15 c. 1) | relazione tecnica (All. 1/2/3 DM 26/6/2015), schede, allegati impianti |
| direttore dei lavori | asseverazione di conformità delle opere al progetto/relazione a fine lavori; sanzione 50% parcella per falsa asseverazione (art. 15 c. 2) | asseverazione DL + APE allegato alla fine lavori |
| impresa / installatore | esecuzione; dichiarazione di conformità impianti (DM 37/2008); libretto d'impianto e prima accensione | DiCo, libretto impianto, rapporto di controllo |
| SUE comunale | riceve relazione ex L. 10 con il titolo, restituisce attestazione di deposito; controlli a campione; riceve asseverazione DL e APE con la fine lavori / SCA | attestazione deposito, verbali di controllo |
| Regione Campania – struttura competente energia (catasto energetico regionale, L.R. 39/2018 mod. L.R. 27/2019; linee guida DGR 100 del 29/2/2024) + ENEA (gestore APE-Campania, SIAPE) | gestione catasto APE e impianti termici, accreditamento certificatori, controlli (min. 2% APE) | codice identificativo APE, ricevuta, verifiche |
| Agenzia Entrate / notaio | clausola e allegazione APE nei contratti registrati | atto con clausola |

## 3. Documenti del pacchetto
Tabella UNICA, in ordine logico di preparazione. Codice = ENE-NN. Blocco A = APE; Blocco B = relazione ex L. 10 e adempimenti impianti.

| Codice | Documento | Obblig. | Prerequisiti (codici) | Gruppo parallelo | Chi lo produce | Validità / scadenza | Nome file standard | Fonte |
|---|---|---|---|---|---|---|---|---|
| ENE-01 | Dati immobile: visura e planimetria catastale, atto/titolo, titoli edilizi e relazioni L. 10 pregresse, APE precedente se esiste | sì | — | P0 | committente / tecnico | — | AAAA-MM-GG_ENE-01_dati-immobile.pdf | [F1] |
| ENE-02 | Documentazione impianti: libretto d'impianto (DM 10/2/2014), rapporti di controllo efficienza energetica, DiCo DM 37/2008, schede tecniche generatore/pompe di calore/FV | sì (APE); condizionato per L. 10: impianti esistenti mantenuti | — | P0 | committente / installatore | libretto: aggiornato a ogni controllo; rapporto: periodicità dPR 74/2013 (es. 4 anni gas < 100 kW, 2 anni > 100 kW — DA VERIFICARE per Campania) | AAAA-MM-GG_ENE-02_libretto-impianti.pdf | [F3][F10] |
| ENE-03 | Incarico e dichiarazione di indipendenza del certificatore (dPR 75/2013 art. 3) | sì (APE) | — | P0 | certificatore | — | AAAA-MM-GG_ENE-03_incarico-indipendenza.pdf | [F11] |
| ENE-04 | Accreditamento/registrazione del certificatore sul portale APE-Campania (procedura della "Guida per la fruizione dell'APE-Campania") | sì (una tantum) | — | P0 | certificatore | — (verificare rinnovi) | AAAA-MM-GG_ENE-04_registrazione-ape-campania.pdf | [F4][F5] |
| ENE-05 | Verbale/rilievo di sopralluogo obbligatorio con foto (involucro, serramenti, generatore, targhe), stratigrafie, misure | sì (APE) | ENE-01, ENE-02 | P1 | certificatore | — | AAAA-MM-GG_ENE-05_sopralluogo-rilievo.pdf | [F2] |
| ENE-06 | Calcolo prestazione energetica (UNI/TS 11300, software certificato CTI) e file XML v5 esteso | sì (APE) | ENE-05 | P2 | certificatore | — | AAAA-MM-GG_ENE-06_calcolo-xml.xml | [F2][F6] |
| ENE-07 | APE firmato (formato DM 26/6/2015 All. 1: classe, EPgl, raccomandazioni) | sì | ENE-06 | P2 | certificatore | 10 anni (art. 6 c. 5), salvo decadenza per mancati controlli impianti o cambio classe | AAAA-MM-GG_ENE-07_ape.pdf | [F1][F2] |
| ENE-08 | Trasmissione al catasto APE-Campania e ricevuta/codice identificativo; consegna al committente entro 15 gg con ricevuta allegata | sì | ENE-07 | P3 | certificatore | 15 gg (DM 26/6/2015 All. 1 p. 7.1.5 come applicato dalla Regione) | AAAA-MM-GG_ENE-08_ricevuta-ape-campania.pdf | [F5][F6] |
| ENE-09 | Clausola contrattuale e allegazione APE (vendita/locazione) o allegazione alla SCA (nuova costruzione / ristrutturazione importante) | sì | ENE-08 | P4 | notaio / committente / tecnico | — | AAAA-MM-GG_ENE-09_ape-allegato-atto-sca.pdf | [F1][F9] |
| ENE-10 | RELAZIONE L.10 – Inquadramento dell'intervento (nuova costruzione, ristrutturazione importante 1°/2° livello, riqualificazione energetica, sostituzione impianto) e scelta dello schema (All. 1, 2 o 3 DM 26/6/2015) | sì (quando dovuta) | ENE-01 | P1 | progettista | — | AAAA-MM-GG_ENE-10_inquadramento-livello.pdf | [F7][F8] |
| ENE-11 | RELAZIONE L.10 – Progetto energetico: stratigrafie, trasmittanze, ponti termici, verifica H'T, Asol, impianti, rinnovabili (D.Lgs. 199/2021 quote), verifica requisiti minimi/edificio di riferimento | sì | ENE-10 | P2 | progettista | — | AAAA-MM-GG_ENE-11_progetto-energetico.pdf | [F7] |
| ENE-12 | RELAZIONE L.10 – Relazione tecnica firmata (schema DM 26/6/2015) + elaborati grafici (piante con zone termiche, schemi impianto) | sì | ENE-11 | P2 | progettista | — | AAAA-MM-GG_ENE-12_relazione-legge10.pdf | [F7][F8] |
| ENE-13 | RELAZIONE L.10 – Deposito al SUE contestuale al titolo (CILA/SCIA/PdC) o comunque prima dell'inizio lavori; ricevuta/attestazione di deposito (in duplice copia dove ancora cartaceo) | sì | ENE-12 | P3 | tecnico → SUE | prima dell'inizio lavori; omesso deposito = sospensione lavori + sanzione | AAAA-MM-GG_ENE-13_deposito-legge10-ricevuta.pdf | [F7][F8] |
| ENE-14 | RELAZIONE L.10 – Varianti in corso d'opera con rilevanza energetica: aggiornamento della relazione e nuovo deposito | condizionato: varianti energetiche | ENE-13 | P3 | progettista | prima dell'esecuzione della variante | AAAA-MM-GG_ENE-14_variante-legge10.pdf | [F8] (prassi, norma non dettagliata) |
| ENE-15 | RELAZIONE L.10 – Asseverazione del DL di conformità delle opere al progetto e alla relazione (art. 8 c. 2), presentata con la dichiarazione di fine lavori | sì | ENE-13, ENE-14 | P4 | direttore lavori | con la fine lavori (CFL) | AAAA-MM-GG_ENE-15_asseverazione-dl-192.pdf | [F7][F8] |
| ENE-16 | Dichiarazione di conformità impianti (DM 37/2008) + libretto d'impianto compilato alla prima accensione + eventuale denuncia INAIL impianto termico > 35 kW | condizionato: impianti nuovi/modificati | ENE-13 | P4 | installatore | — | AAAA-MM-GG_ENE-16_dico-libretto.pdf | [F10] |
| ENE-17 | APE di fine lavori (nuova costruzione / ristrutturazione importante) allegato alla SCA, redatto da certificatore terzo (non progettista né DL) | sì (nuova costruzione / rist. importante) | ENE-15, ENE-16, ENE-03…ENE-08 | P4 | certificatore | 10 anni | AAAA-MM-GG_ENE-17_ape-fine-lavori.pdf | [F1][F7] |
| ENE-18 | Registrazione impianto nel catasto regionale impianti termici (L.R. 39/2018) e rapporto di controllo | condizionato: impianti termici > 10 kW riscaldamento / > 12 kW raffrescamento per i controlli di efficienza (L.R. 39/2018) | ENE-16 | P4 | manutentore / responsabile impianto | periodicità dPR 74/2013 | AAAA-MM-GG_ENE-18_catasto-impianti-rce.pdf | [F12] portale e procedura DA VERIFICARE |

## 4. Flusso (ordine e parallelismi)
APE (vendita/locazione/annuncio):
1. [P0, in parallelo] Dati immobile (ENE-01) · libretto e impianti (ENE-02) · incarico e indipendenza (ENE-03) · registrazione del certificatore su APE-Campania (ENE-04, una tantum).
2. [P1] Sopralluogo obbligatorio (ENE-05). 3. [P2] Calcolo e XML (ENE-06) → APE firmato (ENE-07).
4. [P3] Caricamento XML v5 su APE-Campania → codice/ricevuta (ENE-08); consegna al committente entro 15 gg con ricevuta.
5. [P4] Annuncio con classe e EPgl; clausola e allegazione nell'atto o nel contratto di locazione (ENE-09).
Relazione ex L. 10 (con il titolo edilizio):
1. [P1] Inquadramento e livello (ENE-10), in parallelo con il progetto architettonico.
2. [P2] Progetto energetico e relazione (ENE-11, ENE-12).
3. [P3] Deposito al SUE con CILA/SCIA/PdC (ENE-13) — canale: portale SUE del comune (Napoli: InfoCamere dal 6/7/2026 [F13]) o PEC; torna l'attestazione di deposito, da consegnare al DL/impresa. Varianti → ENE-14.
4. Cantiere: DiCo e libretto (ENE-16).
5. [P4] Fine lavori: asseverazione DL (ENE-15) + APE da certificatore terzo (ENE-17) allegati alla CFL/SCA; registrazione impianto e controlli (ENE-18).
Tempi: il deposito L. 10 deve precedere l'inizio lavori; l'APE va consegnato entro 15 gg dalla trasmissione; per gli edifici venduti "sulla carta" il venditore produce l'APE entro 15 gg dalla richiesta di agibilità [F9]. Controlli regionali a campione (almeno 2% degli APE) [F2].

## 5. Modulistica e canale di invio in Campania
| Ambito | Modulo / portale | Link | Note |
|---|---|---|---|
| Regione Campania (modulistica unificata) | Portale "APE-Campania" (ENEA) per la trasmissione degli APE in XML v5; "Guida per la fruizione dell'APE-Campania" per la registrazione; richiesta copie APE pregressi via modulo + PEC; L.R. 39/2018 (catasto energetico regionale: APE + impianti termici), L.R. 27/2019, DGR 100/2024 linee guida; nota Regione PG 536385/2024 agli Ordini | https://www.apecampania.enea.it/ ; guida: https://www.apecampania.enea.it/doc/Guida_APE_Campania_accessibile.pdf ; nota Regione: https://benevento.ordingegneri.it/wp-content/uploads/sites/74/2024/11/Nota-Regione-PG-536385-Comunicazione-ordini-e-collegi.pdf | Dal 7/1/2025 ore 10 solo XML v5 esteso (CTI); i certificatori già registrati potevano caricare dal 18/11/2024. Relazione ex L. 10: nessun portale regionale, si deposita al SUE con i moduli unificati (CU 27/3/2025, DGR 252/2025) che contengono il quadro "rispetto D.Lgs. 192/2005" [F14] |
| Comune di Napoli | SUE su piattaforma InfoCamere "Impresa in un giorno" dal 6/7/2026 (prima SisDoc): la relazione ex L. 10 si allega al titolo | https://na.camcom.gov.it/print/pdf/node/3192 [F13] | diritti e modalità di deposito separato DA VERIFICARE |
| Comune di Caserta | SUE – deposito con il titolo | DA VERIFICARE | nessuna fonte comunale trovata |
| Comune di Avellino | SUE – deposito con il titolo | DA VERIFICARE | nessuna fonte comunale trovata |
| Comune di Benevento | SUE (RUEC 2016) | https://www.comune.benevento.it/portale/wp-content/uploads/2022/03/Regolamento-Urbanistico-ed-Edilizio-INTEGRALE-con-allegati.pdf | modalità deposito DA VERIFICARE |
| Altri comuni trovati | Frattamaggiore (NA): portale SUE ASMENET con guida; Pisciotta (SA): recepimento moduli unificati DD 217/2025 | vedi scheda SAN [F23][F13] | Differenze trovate: alcuni SUE chiedono ancora il deposito in duplice copia cartacea con timbro di attestazione (prassi descritta in [F8]); altri accettano solo l'allegato nel portale. Nessuna differenza documentata per i quattro capoluoghi (DA VERIFICARE) |

## 6. Scadenze e tempi
- APE: validità 10 anni (art. 6 c. 5 D.Lgs. 192/2005; DM 26/6/2015); decadenza al 31/12 dell'anno successivo al primo controllo impianto non effettuato; rifacimento se cambia la classe [F2][F3]. Consegna entro 15 gg dalla trasmissione regionale [F5].
- Sanzioni art. 15 D.Lgs. 192/2005 (importi da fonti di settore, DA VERIFICARE su normattiva): vendita senza APE € 3.000–18.000; locazione € 300–1.800; annuncio senza indici € 500–3.000; certificatore per APE non conforme € 700–4.200 (+ segnalazione all'Ordine); progettista relazione omessa/non conforme 30% parcella; DL falsa asseverazione 50% parcella; mancata presentazione APE/asseverazione al Comune da parte del DL € 1.000–6.000; costruttore/proprietario senza APE nuova costruzione € 3.000–18.000 [F15][F16].
- Relazione ex L. 10: deposito prima dell'inizio lavori; omissione = sospensione lavori (art. 8) [F8].
- Libretto e controlli: periodicità dPR 74/2013; controlli regionali su impianti > 10 kW / > 12 kW (L.R. 39/2018) [F12].
- DM 28/10/2025 (nuovi requisiti minimi): efficacia 180 gg dalla pubblicazione in GU del 5/12/2025 → dal giugno 2026 (DA VERIFICARE) [F8].

## 7. Errori frequenti e controlli incrociati
- Identificativi catastali, indirizzo, intestatario e CF identici tra APE, atto/contratto, titolo edilizio e relazione L. 10.
- Certificatore non indipendente (ha progettato/diretto l'opera o è parente): APE nullo e sanzione.
- APE senza sopralluogo o senza il codice/ricevuta APE-Campania: non valido per l'atto; XML in versione non v5 respinto dal portale.
- APE scaduto per mancato controllo di efficienza (libretto non aggiornato): rifare.
- Relazione L. 10 depositata dopo l'inizio lavori o non aggiornata alla variante; mancata asseverazione DL a fine lavori → SCA incompleta.
- Dichiarazione "intervento non soggetto al D.Lgs. 192" usata impropriamente (sostituzione generatore, cappotto, serramenti sono soggetti).
- Quote di rinnovabili (D.Lgs. 199/2021) non verificate nelle ristrutturazioni rilevanti.
- Classe energetica dichiarata nell'annuncio diversa dall'APE depositato.

## 8. Collegamenti con altre pratiche
Prima: progetto architettonico e titolo edilizio (CILA/SCIA/PdC) → la relazione ex L. 10 si deposita con il titolo. In parallelo: pratica sismica, DiCo impianti, bonus fiscali (asseverazioni ENEA per ecobonus hanno canale separato). Dopo: CFL con asseverazione DL → SCA con APE → DOCFA. L'APE è richiesto anche per compravendita/locazione dopo sanatoria (scheda SAN) e non dipende dall'autorizzazione paesaggistica (scheda PAE), ma gli interventi su involucro in area vincolata richiedono entrambe. Sostituisce: l'APE sostituisce l'ACE ante 2013; gli APE 2009 restano validi fino a scadenza [F2].

## 9. Fonti
[F1] D.Lgs. 192/2005 artt. 3, 6, 8, 15 — https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-08-19;192 — URL noto, non raggiungibile in sessione il 2026-10-10.
[F2] DM 26/6/2015 "Linee guida APE" (validità 10 anni, controlli, APE 2009) — sintesi ANCE Enna — https://enna.ance.it/2015/07/17/pubblicate-le-nuove-linee-guida-per-l-attestazione-della-prestazione-energetica-degli-edifici/ — 2026-10-10; Ediltecnico "APE: per quanto tempo vale?" — https://ediltecnico.it/?p=9490 — 2026-10-10.
[F3] Ediltecnico "Così si invalida il nuovo APE" (decadenza per controlli impianti) — https://ediltecnico.it/?p=6804 — 2026-10-10.
[F4] Portale APE-Campania (ENEA) — https://www.apecampania.enea.it/ e Guida — https://www.apecampania.enea.it/doc/Guida_APE_Campania_accessibile.pdf — 2026-10-10 (non apribile in sessione).
[F5] Lavori Pubblici, "Attestati di prestazione energetica: in Campania il nuovo catasto digitale" (attivazione 7/1/2025, sostituzione SID) — https://www.lavoripubblici.it/news/attestati-prestazione-energetica-in-campania-nuovo-catasto-digitale-34718 — 2026-10-10; Regione VdA rassegna (comunicazione Regione Campania 2015 su consegna entro 15 gg con ricevuta SID) — https://gestionewww.regione.vda.it/energia/rassegna_stampa/allegati/allegato3239ita.pdf — 2026-10-10.
[F6] Ingenio, "Campania: è stato attivato il nuovo sistema informatico per l'APE" (XML v5, SIAPE) — https://www.ingenio-web.it/articoli/campania-e-stato-attivato-il-nuovo-sistema-informatico-per-l-ape/ — 2026-10-10.
[F7] Ediltecnico, "Relazione tecnica ex Legge 10: quando è obbligatoria e come redigerla" — https://ediltecnico.it/relazione-tecnica-ex-legge-10/ — 2026-10-10.
[F8] Studio Tecnico Pagliai, "Relazione L. 10/91 e D.Lgs. 192/05: deposito all'inizio dei lavori, la variante e sanatoria" — https://www.studiotecnicopagliai.it/relazione-l-10-91-e-d-lgs-192-05-deposito-allinizio-dei-lavori-la-variante-e-sanatoria/ — 2026-10-10; Edilizia.com "Relazione tecnica ex Legge 10" (DM 28/10/2025) — https://www.edilizia.com/leggi-normative/relazione-tecnica-ex-legge-10-cose-quando-e-obbligatoria-e-come-redigerla — 2026-10-10.
[F9] Ediltecnico, "Obblighi di dotazione, informazione, consegna e allegazione dell'APE in caso di vendita o affitto" — https://ediltecnico.it/obblighi-ape-vendita-affitto/ — 2026-10-10; Circolare ANCE 303/2015 (esclusioni art. 3) — https://ragusa.ance.it/wp-content/uploads/archivet/22767-Circolare 303_C_2015.pdf — 2026-10-10.
[F10] dPR 74/2013 e DM 10/2/2014 (libretto) — Ediltecnico "Libretto impianto climatizzazione a macchia di leopardo" — https://ediltecnico.it/libretto-impianto-climatizzazione-macchia-leopardo/ — 2026-10-10.
[F11] dPR 75/2013 requisiti certificatori — Ediltecnico "Requisiti del certificatore energetico" — https://ediltecnico.it/requisiti-del-certificatore-energetico-ecco-i-4-punti-essenziali/ — 2026-10-10; Lavori Pubblici 2014 (tecnici abilitati senza corso dopo DL 145/2013) — https://www.lavoripubblici.it/news/stampa/12858 — 2026-10-10.
[F12] L.R. Campania 20/11/2018 n. 39 (testo) — https://cdn.qualenergia.it/wp-content/uploads/2018/11/CAMPANIA_LR_n39__20_11_2018.pdf — 2026-10-10; QualEnergia "Campania, istituito un catasto unico per APE e impianti termici" — https://www.qualenergia.it/articoli/campania-istituito-un-catasto-unico-per-ape-e-impianti-termici-domestici/ — 2026-10-10; Nota Regione Campania PG 536385 (2024) agli Ordini (DGR 100/2024) — https://benevento.ordingegneri.it/wp-content/uploads/sites/74/2024/11/Nota-Regione-PG-536385-Comunicazione-ordini-e-collegi.pdf — 2026-10-10.
[F13] Camera di Commercio di Napoli, comunicato 2/7/2026 SUE InfoCamere — https://na.camcom.gov.it/print/pdf/node/3192 — 2026-10-10.
[F14] Regione Campania DGR 252/2025 (moduli unificati) — https://www.donnegeometra.it/wp-content/uploads/2025/05/CAMPANIACm_06052025_252.pdf — 2026-10-10.
[F15] Fisco7, "Nuovo APE da ottobre 2015" (sanzioni art. 15) — https://www.fisco7.it/2015/07/nuovo-ape-da-ottobre-2015/ — 2026-10-10.
[F16] ANCE Enna, commento nuove regole APE (sanzioni annunci) — https://enna.ance.it/wp-content/uploads/archivet/13278-commento ance-nuove regole ape.pdf — 2026-10-10.
[F17] Lavori Pubblici, "Rinnovo APE: il MASE sull'obbligo per i contratti di locazione" — https://www.lavoripubblici.it/news/amp/rinnovo-ape-mase-obbligo-per-contratti-locazione-35808 — 2026-10-10.

## 10. Da verificare con il tecnico
1. Testo vigente art. 6, 8 e 15 D.Lgs. 192/2005 (importi sanzioni) su normattiva.
2. Regole attuali del portale APE-Campania: termine di trasmissione/consegna (15 gg), eventuali costi, gestione annullamenti/sostituzioni, richiesta copie APE pregressi.
3. Stato del catasto regionale impianti termici (L.R. 39/2018): portale attivo? chi registra il libretto? soggetti delegati ai controlli (Regione/Province/comuni > 40.000 ab.).
4. Requisiti di accreditamento dei certificatori in Campania (corso regionale e ore, riconoscimento automatico per laureati/diplomati abilitati).
5. Efficacia del DM 28/10/2025 (nuovi requisiti minimi) e nuovi schemi di relazione tecnica.
6. Se i SUE di Napoli, Caserta, Avellino, Benevento richiedono deposito separato della relazione L. 10 (protocollo autonomo) o solo come allegato del titolo.
7. Obbligo APE per rinnovo/proroga di locazione (nota MASE) [F17].
8. Gestione delle varianti energetiche in corso d'opera (nuovo deposito o aggiornamento in fine lavori) secondo i singoli SUE.
9. Quote minime di rinnovabili D.Lgs. 199/2021 applicabili alle ristrutturazioni rilevanti.
10. Controlli a campione regionali: percentuale e modalità in Campania.
