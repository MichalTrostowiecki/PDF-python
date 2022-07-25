import PyPDF2

template = PyPDF2.PdfFileReader(open("twopage.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.merge_page(watermark.getPage(0))
    output.addPage(page)

    with open("new_pdf", "wb") as file:
        output.write(file)
