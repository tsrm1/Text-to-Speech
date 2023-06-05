from gtts import gTTS 
import os
file = open("1.txt", "r", encoding='utf-8').read()

speech = gTTS(text=file, lang='ru', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")