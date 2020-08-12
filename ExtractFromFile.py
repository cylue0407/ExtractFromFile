#Extract text from file(Word, PDF) and validate by regular expression
import RegularEx
import ReadFile
from optparse import OptionParser
import os.path
import time

def add_to_file(myFile, email):
	"""Save in a text file the emails extracted """
	with open(myFile,"a") as emailsfile:
            emailsfile.write(email+",")


if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE] [OUTPUT]")
    # No options added yet. Add them here if you ever need them.
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    if os.path.isfile(args[0]):
        # create file to export emails
        extensionTime = time.strftime("%H%M%S")
        myFile = "emailList_"+extensionTime+".txt"
        #Check File Type
        if(os.path.splitext(args[0])[1] == ".docx"):
            rawText = ReadFile.getTextFromDoc(args[0])
            for item in RegularEx.reEXEmail(str(rawText)):
                print(item)
                add_to_file(myFile, item)
        elif(os.path.splitext(args[0])[1] == ".pdf"):
            rawText = ReadFile.getTextFromPDF(args[0])
            for item in RegularEx.reEXEmail(str(rawText)):
                print(item)
                add_to_file(myFile, item)
    else:
        print("Can't find that file.")

    

#rawText = ReadFile.getTextFromDoc("test.docx")
#print(rawText)
#if RegularEx.reEXEmail(rawText):
#    print("Match Success")
#else:
#    print("Match Failed.")
#RegularEx.reEXEmail("My email is: xx@163.com & xx@gmail.com")
#RegularEx.reEXEmail(rawText)