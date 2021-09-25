from gtts import gTTS
import os

fh=open("test.txt","r")


mytext=fh.read().replace("\n"," ")
languge='en'
output=gTTS(text=mytext,lang=languge,slow=False)
output.save("output.mp3")

fh.close()

os.system("start output.mp3")