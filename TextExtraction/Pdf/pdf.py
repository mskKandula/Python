# pip install PyPDF2

import PyPDF2

with open('sample.pdf',"rb") as file:
    pdfReader = PyPDF2.PdfFileReader(file)
  
    # printing number of pages in pdf file
    print(pdfReader.numPages)
  
    # creating a page object
    pageObj = pdfReader.getPage(0)
  
    # extracting text from page
    print(pageObj.extractText())