from gtts import gTTS
import os
from googletrans import Translator

mytext = input('Enter text: ')

translater= Translator()
translated = translater.translate(text=mytext, dest='sinhala', src='en')

translatedText = translated.text

print(translatedText)

myobj = gTTS(text=translatedText, lang='si', slow=False)
  
myobj.save("text.mp3")
os.system("text.mp3")