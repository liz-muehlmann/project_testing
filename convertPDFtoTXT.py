
def main():

    from pathlib import Path

    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfdevice import PDFDevice
    from pdfminer.layout import LAParams, LTTextBox, LTTextLine
    from pdfminer.converter import PDFPageAggregator
    directory = ".\\PDF\\"
    txt = ".\\txt\\"
    for path in Path(directory).glob("*.pdf"):
        with path.open("rb") as file:
            parser = PDFParser(file)
            document = PDFDocument(parser, "")
            if not document.is_extractable:
                continue

            manager = PDFResourceManager()
            params = LAParams()

            device = PDFPageAggregator(manager, laparams=params)
            interpreter = PDFPageInterpreter(manager, device)

            text = ""

            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                for obj in device.get_result():
                    if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine):
                        text += obj.get_text()
        with open(txt +"{}.txt".format(path.stem), "wb") as file:
            file.write(text.encode('utf8'))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())