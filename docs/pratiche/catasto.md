# CAT — Pratiche catastali: DOCFA, Pregeo, voltura (Catasto Fabbricati e Catasto Terreni)

Regione: Campania · Province: Avellino, Benevento, Caserta, Napoli (Salerno solo se diversa) · Data ricerca: 2026-10-10
Stato della scheda: bozza da verificare con il tecnico. Ogni riga con fonte; quello che non si trova è "DA VERIFICARE".
Nota di metodo: durante la ricerca i siti agenziaentrate.gov.it, normattiva.it e regione.campania.it NON erano raggiungibili direttamente dall'ambiente (accesso bloccato); i contenuti sono stati ricostruiti da riassunti di ricerca web su documenti ufficiali (quaderni/vademecum delle Direzioni Provinciali AE, circolari) e fonti professionali (ordini/collegi). Le cifre vanno ricontrollate sulla pagina ufficiale prima dell'uso.

## 1. Cos'è e quando si usa
Le pratiche catastali aggiornano la banca dati dell'Agenzia delle Entrate – Territorio (ex Agenzia del Territorio) per allineare mappa (Catasto Terreni) e unità immobiliari (Catasto Fabbricati) allo stato reale dopo i lavori o dopo un trasferimento di diritti. Tre famiglie: **Pregeo** (atti di aggiornamento geometrico del Catasto Terreni: tipo mappale, tipo di frazionamento, tipo particellare), **DOCFA** (dichiarazione di nuova costruzione o di variazione al Catasto Fabbricati, con proposta di classamento/rendita) e **voltura** (aggiornamento dell'intestazione dopo un atto o una successione). Norma base: R.D.L. 13 aprile 1939 n. 652 (conv. L. 1249/1939) artt. 20 e 28 come modificati dall'art. 34-quinquies D.L. 10 gennaio 2006 n. 4 conv. L. 9 marzo 2006 n. 80 (termine 30 giorni) [F1][F2]; D.M. 19 aprile 1994 n. 701 (procedura DOCFA, rendita proposta); L. 1° ottobre 1969 n. 679 e D.P.R. 650/1972 (Catasto Terreni e volture); D.Lgs. 18 settembre 2024 n. 139 (tributi catastali dal 1° gennaio 2025) [F6].
Quando NON si usa: non sostituisce i titoli edilizi (CILA/SCIA/PdC) né la CFL/SCA comunale: il DOCFA è un adempimento fiscale e presuppone che lo stato dichiarato sia (o sia stato) legittimato urbanisticamente (art. 19 c. 14 D.L. 78/2010 sulla conformità catastale negli atti). Non serve il DOCFA per lavori che non cambiano consistenza, destinazione, planimetria o rendita (manutenzione ordinaria, tinteggiatura, sostituzione impianti) [F4]. La voltura non serve per atti notarili trasmessi con Modello Unico Informatico (voltura automatica) [F8].

## 2. Chi è coinvolto
| Soggetto | Ruolo | Cosa produce |
|---|---|---|
| committente (proprietario / titolare diritto reale) | dichiarante; firma la dichiarazione DOCFA e la domanda di voltura; paga i tributi | lettera di incarico al tecnico, documento d'identità, titolo di proprietà / atto |
| tecnico abilitato (architetto, ingegnere, geometra, perito edile, agronomo/forestale per i terreni) | redige e firma digitalmente gli atti Pregeo/DOCFA; invia tramite SISTER con la propria utenza; responsabile della proposta di classamento | libretto Pregeo, modello D/1N/2N, elaborato planimetrico, planimetrie, relazione tecnica, ricevute SISTER |
| impresa | non interviene direttamente; fornisce la data di ultimazione lavori (coincidente con la CFL) | dichiarazione di fine lavori (dato) |
| Agenzia delle Entrate – Ufficio Provinciale Territorio (Avellino, Benevento, Caserta, Napoli) | riceve gli atti via SISTER, protocolla, approva automaticamente o con controllo, può rettificare il classamento proposto entro 12 mesi (art. 1 c. 3 D.M. 701/1994) | ricevuta di protocollo, attestato di approvazione (Pregeo), visura aggiornata con rendita proposta/validata, eventuale avviso di rettifica |
| Comune (Portale dei Comuni) | dal 1° luglio 2025 riceve dall'Agenzia i tipi di frazionamento/mappali con stralcio (deposito ex art. 30 c. 5 d.P.R. 380/2001, ora telematico) | nessun documento al tecnico |

## 3. Documenti del pacchetto
Tabella UNICA, in ordine logico di preparazione. Codice = CAT-NN. Gruppi: P0 prerequisiti, P1 Catasto Terreni (Pregeo), P2 Catasto Fabbricati (DOCFA), P3 voltura.

| Codice | Documento | Obblig. | Prerequisiti (codici) | Gruppo parallelo | Chi lo produce | Validità / scadenza | Nome file standard | Fonte |
|---|---|---|---|---|---|---|---|---|
| CAT-01 | Visura catastale attuale (terreni e fabbricati) con intestati, identificativi e rendita | sì | — | P0 | tecnico (SISTER / Fisconline, consultazione gratuita dal 2025) | istantanea: rifare prima dell'invio | AAAA-MM-GG_CAT-01_visura_catastale.pdf | [F6] |
| CAT-02 | Planimetria catastale in atti (ultima registrata) ed elaborato planimetrico esistente | sì (variazioni); no (nuova costruzione senza fabbricato preesistente) | CAT-01 | P0 | tecnico (SISTER, servizio "planimetrie" per il tecnico incaricato) | istantanea | AAAA-MM-GG_CAT-02_planimetria_in_atti.pdf | [F6] |
| CAT-03 | Estratto di mappa digitale (file .emap) per Pregeo, rilasciato dall'Ufficio via SISTER | sì per Pregeo | CAT-01 | P0 | tecnico (richiesta via SISTER) | 6 mesi dal rilascio (dato da verificare); gratuito dal 2025 | AAAA-MM-GG_CAT-03_estratto_mappa_foglioNN.emap | [F5][F6] DA VERIFICARE validità |
| CAT-04 | Lettera di incarico / mandato del committente al tecnico (con dati del dichiarante e CF) | sì | — | P0 | committente (firma) / tecnico (redige) | per la singola pratica | AAAA-MM-GG_CAT-04_lettera_incarico.pdf | [F3] |
| CAT-05 | Copia documento d'identità e CF del/dei dichiaranti | sì | — | P0 | committente | documento in corso di validità | AAAA-MM-GG_CAT-05_documento_identita.pdf | [F3] |
| CAT-06 | Titolo abilitativo edilizio (PdC/SCIA/CILA) + CFL con data di ultimazione, o atto di provenienza | sì (DOCFA: data ultimazione lavori; voltura: atto registrato) | — | P0 | committente / tecnico / notaio | — | AAAA-MM-GG_CAT-06_titolo_edilizio_o_atto.pdf | [F1][F7] |
| CAT-07 | Rilievo topografico celerimetrico/GNSS agganciato ai punti fiduciali (libretto delle misure) | sì per tipo mappale/frazionamento con nuove linee; no per tipo mappale "in deroga"/senza rilievo nei casi ammessi | CAT-03 | P1 | tecnico | — | AAAA-MM-GG_CAT-07_libretto_misure.dat | [F5] DA VERIFICARE casi di esenzione dal rilievo |
| CAT-08 | Atto Pregeo (file .dat Pregeo 10): tipo mappale (TM), tipo di frazionamento (FR), misto (FM), tipo particellare, con relazione tecnica, modello censuario e proposta di aggiornamento | sì quando il fabbricato nuovo/ampliato deve essere inserito in mappa (TM) o la particella va divisa (FR) | CAT-03, CAT-04, CAT-07 | P1 | tecnico (firma digitale) | nessuna scadenza, ma estratto di mappa aggiornato | AAAA-MM-GG_CAT-08_pregeo_TM_foglioNN_partNNN.dat | [F5] |
| CAT-09 | Dichiarazione di tipo mappale/frazionamento sottoscritta dal proprietario (firma sul frontespizio o delega) | sì | CAT-04, CAT-05, CAT-08 | P1 | committente | per la pratica | AAAA-MM-GG_CAT-09_firma_proprietario_pregeo.pdf | [F5] |
| CAT-10 | Ricevuta SISTER Pregeo: protocollo e attestato di approvazione (automatica o dopo controllo) | sì | CAT-08, CAT-09 | P1 (output) | Agenzia Entrate | conservare; prerequisito del DOCFA di nuova costruzione | AAAA-MM-GG_CAT-10_ricevuta_pregeo_protNNNN.pdf | [F5] |
| CAT-11 | Elaborato planimetrico (EP) con elenco subalterni, su file DOCFA | sì quando ci sono 2 o più unità con parti comuni, o beni comuni non censibili; condizionato altrimenti (Circ. 9/T 2001) | CAT-02, CAT-10 (nuova costr.) | P2 | tecnico | — | AAAA-MM-GG_CAT-11_elaborato_planimetrico.pdf | [F3] |
| CAT-12 | Planimetrie delle unità immobiliari (scala 1:200, orientamento, altezze, confini, piano) | sì | CAT-06, CAT-11 | P2 | tecnico | — | AAAA-MM-GG_CAT-12_planimetria_subN.pdf | [F3] |
| CAT-13 | Modello D (quadro dichiarazione: dati dichiarante, causale, data ultimazione lavori, elenco unità, tributi) + modello 1N parte I e II (categorie ordinarie A/B/C) o 2N (speciali D/E) | sì | CAT-04, CAT-05, CAT-06, CAT-11, CAT-12 | P2 | tecnico (compila) / committente (dichiara) | — | AAAA-MM-GG_CAT-13_docfa_modD_1N.pdf | [F3] |
| CAT-14 | Proposta di classamento e rendita (categoria, classe, consistenza; per D/E stima diretta o multiparametrica) | sì | CAT-13 | P2 | tecnico | soggetta a rettifica dell'Ufficio entro 12 mesi | (dentro CAT-13) | [F3] |
| CAT-15 | File DOCFA (.dc3/.dcf) firmato digitalmente, con eventuale "dichiarazione di conformità dello stato dei luoghi" e indicazione del titolo edilizio | sì | CAT-11…CAT-14 | P2 | tecnico | invio entro 30 gg dall'ultimazione | AAAA-MM-GG_CAT-15_docfa_nuova_costruzione.dc3 | [F1][F3] |
| CAT-16 | Ricevuta SISTER DOCFA (protocollo), visura con "rendita proposta" e planimetrie registrate | sì (output) | CAT-15 | P2 (output) | Agenzia Entrate | la rendita diventa definitiva se non rettificata entro 12 mesi | AAAA-MM-GG_CAT-16_ricevuta_docfa_protNNNN.pdf | [F3] DA VERIFICARE termine 12 mesi nel testo del D.M. 701/1994 |
| CAT-17 | Domanda di voltura (Voltura 2.0) con estremi dell'atto/successione, soggetti dante/avente causa, immobili | condizionato: solo se il trasferimento non è già volturato automaticamente (MUI notarile / dichiarazione di successione telematica) | CAT-01, CAT-04, CAT-05, CAT-06 | P3 | tecnico o parte (SISTER / Fisconline / PEC / ufficio) | entro 30 gg dalla registrazione dell'atto | AAAA-MM-GG_CAT-17_voltura_2.0.pdf | [F7][F8] |
| CAT-18 | Ricevuta pagamento tributi: DOCFA e Pregeo 70 € per unità (dal 1/1/2025); voltura 55 € + bollo 16 € | sì | CAT-15 / CAT-08 / CAT-17 | P2/P1/P3 | tecnico (addebito su conto SISTER) o committente (F24 Elide per voltura cartacea) | — | AAAA-MM-GG_CAT-18_ricevuta_tributi.pdf | [F6][F7] |

Regole: il DOCFA di nuova costruzione presuppone che il fabbricato sia già in mappa (tipo mappale approvato, CAT-10); una variazione per ampliamento con nuova sagoma richiede anch'essa il tipo mappale preventivo; una variazione interna (frazionamento/fusione unità, cambio destinazione) non richiede Pregeo [F5]. La voltura non è dovuta per le variazioni DOCFA, che mantengono gli intestati.

## 4. Flusso (ordine e parallelismi)
1. [P0] Verifica catena dei titoli e identificativi: visura (CAT-01), planimetrie in atti (CAT-02), titolo edilizio e data fine lavori (CAT-06). Confronto con lo stato dei luoghi (rilievo). Incarico e documenti del dichiarante (CAT-04, CAT-05).
2. [P1, solo se cambia la mappa] Richiesta estratto di mappa (CAT-03) → rilievo (CAT-07) → redazione Pregeo (CAT-08) → firma proprietario (CAT-09) → invio SISTER → approvazione automatica (di norma in tempo reale per atti conformi) o esito del controllo d'ufficio; cosa torna: protocollo + attestato di approvazione (CAT-10). Dal 1° luglio 2025 il deposito del frazionamento al Comune è fatto dall'Agenzia sul Portale dei Comuni (Ris. 40/E/2025) [F5].
3. [P2] Con mappa aggiornata: elaborato planimetrico (CAT-11), planimetrie (CAT-12), modelli D/1N (CAT-13), classamento (CAT-14), file DOCFA (CAT-15). Invio SISTER con addebito tributi (CAT-18). Cosa torna: ricevuta con protocollo, registrazione in banca dati con "rendita proposta" (CAT-16). L'Ufficio può controllare e rettificare entro 12 mesi; in assenza, la rendita proposta diventa definitiva [F3].
4. [P3, in parallelo con P2 se c'è stato un atto non volturato] Domanda di voltura (CAT-17) entro 30 gg dalla registrazione; cosa torna: ricevuta e visura con nuovi intestati [F7].
5. Dopo: la ricevuta DOCFA è allegato della SCA (art. 24 c. 5 d.P.R. 380/2001) e dell'atto notarile (conformità catastale, art. 29 c. 1-bis L. 52/1985).
Canale: esclusivamente telematico tramite SISTER (tecnici abilitati con convenzione) [F3][F5]; per la voltura anche Fisconline/Entratel del cittadino, PEC o sportello dell'Ufficio Provinciale [F7]. Tempi: approvazione Pregeo automatica immediata o controllo d'ufficio (termine non trovato: DA VERIFICARE); DOCFA registrato subito con rendita proposta; voltura lavorata dall'ufficio (tempi non trovati: DA VERIFICARE).

## 5. Modulistica e canale di invio in Campania
| Ambito | Modulo / portale | Link | Note |
|---|---|---|---|
| Agenzia Entrate (nazionale, vale per tutta la Campania) | Software DOCFA 4.00.5 (giugno 2025) + archivio provinciale; Pregeo 10 (versione corrente DA VERIFICARE); SISTER | https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-fabbricati-docfa ; https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-terreni-pregeo ; https://sister.agenziaentrate.gov.it | Archivio provinciale di Caserta aggiornato con release di aprile 2026 (scaricare l'archivio della provincia prima di redigere) [F9] |
| Voltura (nazionale) | Voltura 2.0 (software) / "Voltura catastale" in area riservata | https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/voltura-catastale | 55 € tributo + 16 € bollo per domanda/Comune/catasto [F7] |
| Ufficio Provinciale Territorio Napoli | sportello su appuntamento (CUP/area riservata) | DA VERIFICARE | Prontuario DOCFA della DP Caserta (prot. 108864/2020) usato come riferimento locale [F10] |
| Ufficio Provinciale Territorio Caserta | come sopra; vademecum DOCFA DP Caserta 2020 | https://caserta.ordingegneri.it/wp-content/uploads/sites/113/2023/09/vademecum-DOCFA_entrate_agedp-ce_108864_2020_1784_all1.pdf | archivio provinciale aggiornato 2026 [F9][F10] |
| Ufficio Provinciale Territorio Avellino | DA VERIFICARE | — | nessuna disposizione locale trovata |
| Ufficio Provinciale Territorio Benevento | DA VERIFICARE | — | nessuna disposizione locale trovata |
| Comuni (Napoli, Caserta, Avellino, Benevento) | nessun modulo: le pratiche catastali non passano dal SUE; il deposito frazionamenti ex art. 30 d.P.R. 380/2001 è ora fatto dall'Agenzia sul Portale dei Comuni | — | differenze comunali: nessuna rilevante per il catasto; verificare se il SUE chiede la ricevuta DOCFA in allegato a SCA/CFL (prassi comune) [F5] |
Differenze tra province: le regole sono nazionali; cambiano solo prassi locali (prontuari provinciali) e gli archivi provinciali del software. Marca da bollo: non dovuta per DOCFA/Pregeo (solo tributi speciali); dovuta per la voltura (16 € ogni 4 pagine) [F7].

## 6. Scadenze e tempi
- DOCFA nuova costruzione: entro 30 giorni dal momento in cui il fabbricato è divenuto abitabile o servibile all'uso (art. 28 R.D.L. 652/1939 mod. art. 34-quinquies D.L. 4/2006 conv. L. 80/2006) [F1][F2].
- DOCFA variazione: entro 30 giorni dalla data di ultimazione dei lavori di variazione (art. 20 R.D.L. 652/1939, stessa modifica) [F1][F2]. La data va indicata nel modello D e deve coincidere con la CFL [F2].
- Sanzione per omessa/tardiva dichiarazione: art. 31 R.D.L. 652/1939, importi riportati da fonti professionali come da 1.032 € a 8.264 € per unità (rideterminati dal 2011); riduzione con ravvedimento (art. 13 D.Lgs. 472/1997) a 1/10 del minimo se entro 90 gg, altre riduzioni oltre: IMPORTI DA VERIFICARE sulla pagina AE / lettera dell'Ufficio Provinciale [F11][F12].
- Tipo mappale: obbligatorio prima del DOCFA (art. 8 L. 679/1969; art. 1 c. 5 D.M. 701/1994: dichiarazione al CF solo dopo l'inserimento in mappa); nessun termine autonomo diverso dai 30 gg del DOCFA (DA VERIFICARE).
- Voltura: entro 30 giorni dalla registrazione dell'atto (art. 3 D.P.R. 650/1972); sanzione per ritardo (art. 12 D.P.R. 650/1972) con ravvedimento a importi fissi ridotti (es. 1,50 € entro 90 gg … 2,50 € oltre, nota DP Grosseto 2025) e prescrizione al 31/12 del 5° anno: DA VERIFICARE importi base [F7][F13].
- Controllo del classamento proposto: l'Ufficio può rettificare la rendita proposta entro 12 mesi dalla presentazione (art. 1 c. 3 D.M. 701/1994); decorso il termine la rendita si intende confermata (DA VERIFICARE testo) [F3].
- Tributi dal 1° gennaio 2025 (D.Lgs. 139/2024): DOCFA 70 € per ogni UIU (anche beni comuni); Pregeo 70 € per ogni unità oggetto di autonomo censimento; consultazioni telematiche ed estratti di mappa gratuiti; voltura 55 € + bollo [F6][F7].

## 7. Errori frequenti e controlli incrociati
- Data di ultimazione lavori nel modello D ≠ data della CFL/dichiarazione del DL: è l'errore più segnalato dagli Uffici e fa scattare la sanzione per tardività [F12].
- Identificativi catastali (foglio, particella, subalterno) devono coincidere tra titolo edilizio, Pregeo approvato, DOCFA, SCA e atto notarile; una variazione DOCFA su particella non ancora aggiornata in mappa viene respinta.
- Intestazione catastale ≠ committente/titolare del titolo edilizio: verificare volture pendenti (CAT-17) prima del DOCFA; il dichiarante deve essere intestatario o titolare di diritto (o dichiarare la qualità).
- Codice fiscale e generalità del dichiarante identici in lettera di incarico, modello D e documento d'identità.
- Planimetrie: orientamento, scala, altezze interne, piano e confini (ditte confinanti/strade) obbligatori; porzioni comuni rappresentate solo nell'EP; difformità tra planimetria e progetto allegato alla SCIA/CFL generano problemi in sede di SCA e di atto.
- Rendita proposta pari a zero per D/E non è ammessa (D.M. 701/1994) [F3].
- Tributi dichiarati ≠ calcolati dal software (Pregeo): SISTER respinge l'invio [F5].
- Estratto di mappa scaduto o non "ufficiale" dell'Ufficio: impedisce l'approvazione automatica del Pregeo [F5].
- Versione software non aggiornata o archivio provinciale non corrispondente (es. Caserta 2026): file non accettato [F9].

## 8. Collegamenti con altre pratiche
Prima: titolo edilizio (CILA/SCIA/PdC) → eventuale pratica sismica (deposito/autorizzazione, scheda SIS) → esecuzione → CFL con data di ultimazione. Poi: Pregeo (TM/FR) → DOCFA entro 30 gg → SCA (allegato: ricevuta DOCFA e planimetrie, art. 24 d.P.R. 380/2001) → atto notarile (conformità catastale). In parallelo: voltura se c'è stato un trasferimento non automatico; dichiarazione di successione (che include la voltura). Sostituzioni: la voltura automatica da MUI notarile sostituisce la domanda; il DOCFA "variazione per esatta rappresentazione grafica" senza lavori non sostituisce la sanatoria urbanistica.

## 9. Fonti
[F1] Agenzia del Territorio – disposizione Ufficio Provinciale di Roma 3/5/2006 su art. 34-quinquies D.L. 4/2006 (termine 30 gg) — https://www.geototus.altervista.org/normativa/2006/sanzione%20accatastamento03-05-2006.pdf — 2026-10-10
[F2] Agenzia Entrate DP Brescia, nota 9 agosto (sanzioni DOCFA, artt. 20 e 28 R.D.L. 652/1939) — https://brescia.ordingegneri.it/wp-content/uploads/sites/81/2023/03/Agenzia_Entrate_9_agosto.pdf — 2026-10-10
[F3] Agenzia Entrate – Vademecum DOCFA ver. 1.0 e Linee guida DOCFA 1/2020 — https://www.agenziaentrate.gov.it/portale/documents/20143/257980/Vademecum_Docfa_ver1.0.pdf ; https://www.agenziaentrate.gov.it/portale/documents/20143/3004696/Linee+Guida+Docfa+1_2020.pdf — 2026-10-10 (non apribile dall'ambiente; contenuto da riassunto)
[F4] LavoriPubblici.it – variazioni catastali obbligatorie entro 30 gg — https://www.lavoripubblici.it/news/superbonus-controllo-variazioni-catastali-ecco-come-fare-34769/2 — 2026-10-10
[F5] Agenzia Entrate – Risoluzione 40/E del 9/6/2025 e comunicato 1/7/2025 (frazionamenti al Portale dei Comuni); Quotidianopiù — https://www.quotidianopiu.it/dettaglio/11510531/catasto-terreni-deposito-telematico-dei-frazionamenti ; https://www.studiocerbone.com/?p=500242 — 2026-10-10
[F6] Collegio Geometri Venezia – Tariffe catastali e ipotecarie dal 2025 (D.Lgs. 139/2024: 70 € DOCFA/Pregeo) — https://www.geometri.ve.it/wp-content/uploads/2025/02/TARIFFE-CATASTALI-E-IPOTECARI-DAL-2025.pdf ; https://federazionelombardia.conaf.it/novita-2025-in-materia-di-consultazione-banche-dati-e-presentazione-atti-catastali/ — 2026-10-10
[F7] Ordine Ingegneri – presentazione "Voltura 2.0" (55 € + 16 € bollo, 30 gg) — https://ordingegneri.it/wp-content/uploads/sites/118/2024/07/Voltura-2.0-.pdf — 2026-10-10
[F8] LavoriPubblici.it – voltura per successione e automatismi 2025 — https://www.lavoripubblici.it/news/voltura-catastale-successione-come-quando-farla-35649 — 2026-10-10
[F9] Fiscal Focus – aggiornamento DOCFA 4.00.5/Docte, archivio provinciale Caserta (27/4/2026); LavoriPubblici.it – DOCFA 4.00.5 — https://www.fiscal-focus.it/docfa-docte-aggiornamenti-27-aprile-2026,3,183992 ; https://www.lavoripubblici.it/news/docfa-4005-software-catasto-novita-2025-35881 — 2026-10-10
[F10] Agenzia Entrate DP Caserta – Prontuario/vademecum DOCFA prot. 108864/2020 — https://caserta.ordingegneri.it/wp-content/uploads/sites/113/2023/09/vademecum-DOCFA_entrate_agedp-ce_108864_2020_1784_all1.pdf — 2026-10-10
[F11] UNITEL – Le sanzioni in materia catastale — https://www.unitel.it/notizie/catasto/le-sanzioni-in-materia-catastale — 2026-10-10
[F12] Agenzia Entrate DP Palermo, nota prot. 164800/2021 (sanzioni DOCFA, data ultimazione) — https://palermo.ordingegneri.it/wp-content/uploads/sites/43/2021/10/AGEDP-PA_164800_2021_1712.pdf — 2026-10-10
[F13] Agenzia Entrate DP Grosseto, nota prot. 68389/2025 (voltura: 30 gg, ravvedimento) — https://grosseto.ordingegneri.it/wp-content/uploads/sites/87/2025/10/AGEDP-GR_68389_2025_1698.pdf — 2026-10-10
[F14] Agenzia Entrate – Circolare 9/T/2001 (elaborato planimetrico) — https://www1.agenziaentrate.gov.it/mt/circolari/circolari_2001/circolare_9_2001.pdf — 2026-10-10

## 10. Da verificare con il tecnico
1. Importi vigenti della sanzione art. 31 R.D.L. 652/1939 e misure del ravvedimento applicate dagli Uffici di Napoli/Caserta/Avellino/Benevento (lettere di irrogazione locali).
2. Testo vigente art. 1 c. 3 D.M. 701/1994: termine di 12 mesi per la rettifica della rendita proposta.
3. Validità temporale dell'estratto di mappa Pregeo e casi di tipo mappale senza rilievo (es. fabbricati inferiori a 20 mq, "in deroga").
4. Versione corrente di Pregeo 10 e di DOCFA (4.00.5 + archivio Caserta 2026) accettate da SISTER alla data di invio.
5. Se il dichiarante DOCFA deve allegare copia del documento d'identità nel file (campo "documento" del modello D) oppure se basta la lettera di incarico conservata dal tecnico.
6. Modalità di addebito tributi SISTER dello studio (conto prepagato/convenzione) e chi anticipa i 70 €/UIU.
7. Prassi dei SUE di Napoli/Caserta/Avellino/Benevento: richiesta della ricevuta DOCFA in allegato a SCA/CFL.
8. Importi base della sanzione voltura (art. 12 D.P.R. 650/1972) oltre il ravvedimento.
9. Trattamento dei beni comuni non censibili (BCNC) ai fini del tributo di 70 € dal 2025.
10. Obbligo di tipo mappale per ampliamenti minori (sagoma invariata in pianta ma volume aumentato: sopraelevazione) — prassi dell'Ufficio Provinciale.
