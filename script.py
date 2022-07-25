import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_lisT):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lisT:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)
