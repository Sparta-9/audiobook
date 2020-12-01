import pypdf2
import pyttsx3
book=open("hacking.pdf","rb")
pdfReader = pypdf2.pdfFileReader(book)
pageg = pdfreader.numPages
print(pages)
orator = pyttsx3.init()
page = pdfReader.getpage(11)
for num in range(15,pages):
    page = pdfReader.getpage(11)
    text = page.extractText()
    orator.say(text)
    orator.runAndWait()
