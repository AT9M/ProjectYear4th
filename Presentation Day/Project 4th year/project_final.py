#!/usr/bin/env python3

# pip install SpeechRecognition

# https://pypi.python.org/pypi/SpeechRecognition/
# recognizer_instance.recognize_google(audio_data, key = None, language = "en-US", show_all = False)
# Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
# The Google Speech Recognition API key is specified by key. If not specified, it uses a generic key that works out of the box.
# This should generally be used for personal or testing purposes only, as it may be revoked by Google at any time.

# NOTE: this example requires PyAudio because it uses the Microphone class
import os,random
import speech_recognition as sr
from twilio.rest import Client
import requests
import webbrowser
# obtain audio from the microphone
r = sr.Recognizer()
import wikipedia
import pyttsx3
import urllib.request
import json


engine = pyttsx3.init()
voices = engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # voice selection

account_sid ="AC2b2a88fc50" # Put your Twilio account SID here

auth_token ="1b67d5bd" # Put your auth token here


Number_list = ["+336728"]


engine.say("I'm listening")
engine.runAndWait()


def Wikipedia():
    print(">>>")
    engine.say("What subject ?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        gg= r.recognize_google(audio, language = "en-US")
    except Exception as e:
        print("Error: Could not understand    Example: New york City")
        gg= "New York city"
    try:
        print(wikipedia.summary(gg,sentences=3,auto_suggest=True, redirect=True))
        engine.say(wikipedia.summary(gg,sentences=3,auto_suggest=True, redirect=True))
        engine.runAndWait()
    except wikipedia.DisambiguationError as e:
        wikipedia.random(pages=1)
    return
def SMS():
    
   
    print(">>>")
    engine.say("What do you want to send ?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
        print("Google Speech Recognition thinks you said in fr: -  " + r.recognize_google(audio, language = "fr-FR"))

    except Exception as e:
        print("Error: " + str(e))
    try:
        gg= r.recognize_google(audio, language = "en-US")
    except Exception as e:
        print("Error:  Could not understand  Test Example = Wikipedia")
        gg = "Project Demonstartion"
    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+12057513314", # Put your Twilio number here

        body="This is a message send to you via the Smart Jacket -->"+gg)
    
    engine.say("SMS send")
    engine.runAndWait()
    return 


def emergency():
    engine.say("Trigger emergency signal")
    engine.runAndWait()
    
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        string_data = ""+str(data)


   

    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+12057513314", # Put your Twilio number here

        body="Jacket alert system SEND LAST COORDONATE : --   "+string_data)
    return


while(True):
   
    print(">>>")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
        #print("Google Speech Recognition thinks you said in fr: -  " + r.recognize_google(audio, language = "fr-FR"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    try:
        Commande = r.recognize_google(audio, language = "en-US")
    except Exception as e:
        print("Error:  Could not understand  Test Example = Wikipedia") 
        Commande="Wikipedia"
        
    if(Commande == "send SMS")or(Commande == "SMS"):
        SMS()
        
    elif(Commande == "emergency"):
        emergency()
        
    elif(Commande == "Wikipedia"):
        Wikipedia()
    elif((Commande == "Stop")or(Commande == "stop")):
        engine.say("Shuting down")
        engine.runAndWait()
        break
    else:
        pass
print(">>>")

