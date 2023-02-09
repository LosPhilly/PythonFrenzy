import PyPDF2
pdf_file = open("example.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)


for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    print(page.extract_text())
pdf_file.close()
