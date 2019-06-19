#sudo  apt-get install portaudio19-dev python-pyaudio python3-pyaudio
#pip3 install speechrecognition
import speech_recognition as sr
import sys
import os
r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
try:
    #print("System Output"+r.recognize_google(audio))
    speech = r.recognize_google(audio)
    os.mkdir(speech)
except Exception:
    print("Unable to read")
