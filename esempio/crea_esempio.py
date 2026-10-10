#!/usr/bin/env python3
"""
crea_esempio.py - crea un archivio finto per provare il gestionale senza il NAS.

    python crea_esempio.py          crea esempio/archivio con clienti e file inventati

I PDF sono veri (una pagina con una riga di testo), così l'anteprima funziona.
Nessun dato reale: nomi e numeri sono inventati.
"""
import os
import random
import time

QUI = os.path.dirname(os.path.abspath(__file__))
ARCHIVIO = os.path.join(QUI, "archivio")


def pdf(testo):
    """PDF minimo a una pagina, senza librerie esterne."""
    contenuto = f"BT /F1 18 Tf 60 740 Td ({testo}) Tj ET".encode("latin-1", "replace")
    oggetti = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(contenuto)).encode() + b" >>\nstream\n" + contenuto + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = b"%PDF-1.4\n"
    offs = []
    for i, o in enumerate(oggetti, 1):
        offs.append(len(out))
        out += f"{i} 0 obj\n".encode() + o + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(oggetti)+1}\n0000000000 65535 f \n".encode()
    for o in offs:
        out += f"{o:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(oggetti)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return out


ALBERO = {
    "01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/00_Incarico": [
        ("2025-02-10_Carta-identita_Rossi.pdf", "Carta d'identita - Rossi Mario (esempio)"),
        ("2025-02-10_Procura_Rossi.pdf", "Procura speciale al tecnico (esempio)"),
        ("2025-02-12_Contratto-appalto_Bianchi.pdf", "Contratto d'appalto Bianchi Costruzioni (esempio)")],
    "01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/02_Comune": [
        ("2025-03-01_CILA_prot-1234.pdf", "CILA prot. 1234 del 01/03/2025 (esempio)"),
        ("2025-03-15_CIL_prot-1300.pdf", "Comunicazione inizio lavori prot. 1300 (esempio)"),
        ("2025-03-15_Notifica-preliminare.pdf", "Notifica preliminare ASL (esempio)")],
    "01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/03_Progetto": [
        ("2025-02-20_Tav-01_Stato-di-fatto.pdf", "Tavola 1 stato di fatto (esempio)"),
        ("2025-02-20_Tav-02_Progetto.pdf", "Tavola 2 progetto (esempio)"),
        ("2025-09-30_Tav-03_Stato-finale.pdf", "Tavola 3 stato finale (esempio)"),
        ("Relazione-tecnica.txt", "Relazione tecnica asseverata. Ultimazione lavori: 30/09/2025. (testo di esempio)")],
    "01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/04_Lavori": [
        ("2025-10-02_Certificato-ultimazione-lavori.pdf", "Certificato di ultimazione lavori 30/09/2025 (esempio)"),
        ("2025-10-02_Certificato-regolare-esecuzione.pdf", "Certificato di regolare esecuzione (esempio)"),
        ("2025-10-02_Dichiarazione-DL-conformita.pdf", "Dichiarazione del DL di conformita al titolo (esempio)"),
        ("2025-10-05_Dichiarazione-conformita-impianto-elettrico.pdf", "Dichiarazione di conformita DM 37/2008 - elettrico (esempio)"),
        ("2025-10-06_FIR-rifiuti.pdf", "Formulario rifiuti (esempio)"),
        ("2025-10-08_Ricevuta-DOCFA.pdf", "Ricevuta DOCFA prot. 55555 (esempio)")],
    "01_CLIENTI/Rossi_Mario/2025-003_Rossi_Via-Roma/05_Foto": [
        ("Foto-01.jpg", None), ("Foto-02.jpg", None), ("Foto-03.jpg", None), ("Foto-04.jpg", None), ("Foto-05.jpg", None)],
    "01_CLIENTI/Verdi_Anna/2026-001_Verdi_Via-Napoli/00_Incarico": [
        ("2026-01-15_Carta-identita_Verdi.pdf", "Carta d'identita - Verdi Anna (esempio)")],
    "01_CLIENTI/Verdi_Anna/2026-001_Verdi_Via-Napoli/02_Comune": [
        ("2026-02-01_SCIA_prot-77.pdf", "SCIA prot. 77 (esempio)")],
    "02_FORNITORI/Bianchi_Costruzioni": [
        ("2025-09-20_DURC_Bianchi.pdf", "DURC Bianchi Costruzioni - richiesta 20/09/2025 (esempio)"),
        ("2025-08-01_Visura-camerale_Bianchi.pdf", "Visura camerale Bianchi Costruzioni (esempio)"),
        ("2025-01-10_Polizza-RC_Bianchi.pdf", "Polizza RC (esempio)"),
        ("2025-03-10_Organico-medio_Bianchi.pdf", "Dichiarazione organico medio annuo e CCNL (esempio)")],
    "02_FORNITORI/Elettro_Service": [
        ("2025-10-05_Visura-camerale_ElettroService.pdf", "Visura camerale Elettro Service (esempio)")],
    "03_STUDIO/Modelli": [
        ("Modulo-CFL-Regione-Campania.pdf", "Modulo unificato comunicazione fine lavori (vuoto, esempio)"),
        ("Modulo-CIL-Regione-Campania.pdf", "Modulo unificato comunicazione inizio lavori (vuoto, esempio)")],
    "00_INBOX": [("Scansione_001.pdf", "Scansione senza nome (esempio)"), ("Documento 30.pdf", "Documento senza nome (esempio)")],
}

# jpg minimo (1x1, grigio) per avere file immagine veri
JPG = bytes.fromhex(
    "ffd8ffe000104a46494600010100000100010000ffdb004300080606070605080707070909080a0c140d0c0b0b0c1912130f141d1a1f1e1d1a1c1c20242e2720222c231c1c2837292c30313434341f27393d38323c2e333432"
    "ffc0000b080001000101011100ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffda0008010100003f00fbd3ffd9")


def main():
    random.seed(1)
    n = 0
    for cart, voci in ALBERO.items():
        d = os.path.join(ARCHIVIO, *cart.split("/"))
        os.makedirs(d, exist_ok=True)
        for nome, testo in voci:
            p = os.path.join(d, nome)
            if os.path.exists(p):
                continue
            with open(p, "wb") as f:
                if nome.endswith(".pdf"):
                    f.write(pdf(testo))
                elif nome.endswith(".jpg"):
                    f.write(JPG)
                else:
                    f.write(testo.encode("utf-8"))
            # date di modifica verosimili, prese dal nome quando c'è
            m = nome[:10]
            try:
                t = time.mktime(time.strptime(m, "%Y-%m-%d"))
            except ValueError:
                t = time.time() - random.randint(1, 400) * 86400
            os.utime(p, (t, t))
            n += 1
    print(f"Creati {n} file in {ARCHIVIO}")


if __name__ == "__main__":
    main()
