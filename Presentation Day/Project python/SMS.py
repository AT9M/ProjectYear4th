# NOTE: this example requires PyAudio because it uses the Microphone class
import os,random
import subprocess
import speech_recognition as sr
from twilio.rest import Client
import requests
import webbrowser
import pyttsx3
engine = pyttsx3.init()
# obtain audio from the microphone
r = sr.Recognizer()
import wikipedia
#voices = engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # voice selection
import shlex

def SMS():


    print(">>>")
    engine.say("What do you want to send ?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
    print("Google Speech Recognition thinks you said in fr: -  " + r.recognize_google(audio, language = "fr-FR"))

    gg= r.recognize_google(audio, language = "en-US")
    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+447588675953", # Put your Twilio number here

        body="This is a message send to you via the Smart Jacket -->"+gg)


    return
