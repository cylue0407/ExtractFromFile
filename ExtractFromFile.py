#Extract text from file(Word, PDF) and validate by regular expression
import RegularEx
import ReadFile

rawText = ReadFile.getTextFromDoc("test.docx")
#print(rawText)
#if RegularEx.reEXEmail(rawText):
#    print("Match Success")
#else:
#    print("Match Failed.")
#RegularEx.reEXEmail("My email is: xx@163.com & xx@gmail.com")
RegularEx.reEXEmail(rawText)