#Extract text from file(Word, PDF) and validate by regular expression
import RegularEx
import ReadFile

rawText = ReadFile.getTextFromDoc('test.docx')
print(rawText)
if RegularEx.reEXBirth(rawText):
    print("Match Success")
else:
    print("Match Failed.")