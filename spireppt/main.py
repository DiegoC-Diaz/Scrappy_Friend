from PyPDF2 import PdfReader


reader=PdfReader("RTAudio_Presentation.pdf")

print(len(reader.pages))

page=reader.pages[7]
text=page.extract_text()
print(text)