from PyPDF2 import PdfReader

def erstelle_glossar(pdf_datei, woerter, ausgabe_datei):

    glossar = {}

    with open(pdf_datei, 'rb') as pdf_datei:
        pdf_reader = PdfReader(pdf_datei)


        # check if its work
        for seitennummer, seite in enumerate(pdf_reader.pages):
            text = seite.extract_text()
            print(f'Seite {seitennummer + 1}:\n{text}\n')

        for seitennummer, seite in enumerate(pdf_reader.pages):
            text = seite.extract_text()

            for wort in woerter:
                if wort.lower() in text.lower():
                    if wort not in glossar:
                        glossar[wort] = []
                    glossar[wort].append(seitennummer + 1)  # Seitennummer beginnt bei 1

    with open(ausgabe_datei, 'w') as datei:
        for wort, seiten in glossar.items():
            seiten_str = ', '.join(map(str, seiten))
            datei.write(f'{wort}: Seite(s) {seiten_str}\n')


# Beispielaufruf
pdf_datei = 'mypdffile.pdf'
woerter = ['Zählernummer',"Seite"]
ausgabe_datei = 'glossar.txt'

erstelle_glossar(pdf_datei, woerter, ausgabe_datei)


