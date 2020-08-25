# This program can rotate, merge pdfs, add water mark to pdfs
import PyPDF2
import sys

with open('dummy.pdf', 'rb') as file:
    # Read as binary file
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    # Read the number of pages in pdf
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilteddummy.pdf', 'wb') as new_file:
        writer.write(new_file)


inputs = sys.argv[1:]
def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('Mergedpdf.pdf')


def watermark_pdf():
    pdf = PyPDF2.PdfFileReader(open('Mergedpdf.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    writer = PyPDF2.PdfFileWriter()

    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        page.mergePage(watermark.getPage(0))
        writer.addPage(page)

    with open('Watermarkedpdf.pdf', 'wb') as file:
        writer.write(file)


pdf_merger(inputs)
watermark_pdf()