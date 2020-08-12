#Extract Text from File(Word, PDF)
import PyPDF2
import docx

def getTextFromPDF(filePath):
    pdfDoc = open(filePath,'rb')
    pdfRdr = PyPDF2.PdfFileReader(pdfDoc)
    num_page = pdfRdr.getNumPages()
    pdfText = ""
    for page_count in range(num_page):
        pdfText += pdfRdr.getPage(page_count).extractText()
    result = pdfText
    pdfDoc.close()
    return result

def getTextFromDoc(filePath):
    docObj = docx.Document(filePath)
    paraList = docObj.paragraphs
    paraText = ''
    for para in paraList:
        paraText += para.text
    result = paraText
    return result