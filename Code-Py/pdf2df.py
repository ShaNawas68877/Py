import pandas
import PyPDF2

pdfFileObj = open('table.pdf', 'rb') #C:\Users\Shanawas\Desktop
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
page1 = pageObj.extractText()

page1 = page1[25:]
print(page1, end ='')
