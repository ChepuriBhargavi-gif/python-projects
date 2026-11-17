# from pypdf import PdfReader
# from gtts import gTTS
# tts = gTTS("Hello world",lang='en')
# tts.save("demo.mp3")




from gtts import gTTS
from pypdf import PdfReader

reader = PdfReader("adv_func_task-1-1-1-1 (1).pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() or ""

tts = gTTS(text=text,lang='en')

tts.save("Advanced Functions.mp3")

print("PDF successfully converted into audio!")
