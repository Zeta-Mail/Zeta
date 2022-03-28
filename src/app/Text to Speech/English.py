from gtts import gTTS
import os

mytext = input('Enter text: ')

myobj = gTTS(text=mytext, lang='en', slow=False)
  
myobj.save("text.mp3")
os.system("text.mp3")