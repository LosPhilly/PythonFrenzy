import PyPDF2
pdf1 = PyPDF2.PdfReader(open("pdf1.pdf", "rb"))
pdf2 = PyPDF2.PdfReader(open("pdf2.pdf", "rb"))
pdf3 = PyPDF2.PdfReader(open("pdf3.pdf", "rb"))
pdf_merger = PyPDF2.PdfWriter()

for page in range(len(pdf1.pages)):
    pdf_merger.add_page(pdf1.pages[page])

for page in range(len(pdf2.pages)):
    pdf_merger.add_page(pdf2.pages[page])

for page in range(len(pdf3.pages)):
    pdf_merger.add_page(pdf3.pages[page])
merged_pdf = open("merged_pdf.pdf", "wb")
pdf_merger.write(merged_pdf)
merged_pdf.close()
