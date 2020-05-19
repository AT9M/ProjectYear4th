#!/usr/bin/env python3.6.8

import os,random
import subprocess
import speech_recognition as sr
from twilio.rest import Client
import requests
import webbrowser
import pyttsx3
engine = pyttsx3.init()
r = sr.Recognizer()
import wikipedia

import shlex
account_sid ="AC6a6f62dbaf928dab9d849e25d1412efb"

auth_token ="25380b677c458cbfca4abc0eea9bdce0"


Number_list = ["+33617966728","+33617966728"]

print(">>>")
engine.say("I'm listening")
engine.runAndWait()
#subprocess.call(["espeak","I'm Listening"])

print(sr.Microphone.list_microphone_names())


def Wikipedia():
    print(">>>")
    engine.say("What subject ?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Analizying...")
    gg= r.recognize_google(audio, language = "en-US")
    print(wikipedia.summary(gg,sentences=3,auto_suggest=True, redirect=True))
    try:
        engine.say(wikipedia.summary(gg,sentences=3,auto_suggest=True, redirect=True))
        engine.runAndWait()
    except wikipedia.DisambiguationError as e:
        print("disambiguation")
    return

def SMS():


    print(">>>")
    engine.say("What do you want to send ?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Analizying...")
    gg= r.recognize_google(audio, language = "en-US")
    ggfr = r.recognize_google(audio, language = "fr-FR")
    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), 

        from_="+447588675953", 

        body="This is a message send to you via the Smart Jacket -->"+gg+" or you have said in French :"+ggfr)


    return


def emergency():
    engine.say("EMERGENCY PROTOCOL ACTIVATED !")
    engine.runAndWait()
    def display_position():
        """  Function To Print GeoIP Latitude & Longitude """
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        geo_data = geo_request.json()

        a=("latitude "+geo_data['latitude'],"longitude "+geo_data['longitude'])

        str =  ' --   '.join(a)
        return str



    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i),

        from_="+447588675953", 

        body="Jacket alert system SEND LAST COORDONATE : --   "+display_position())
    return

while True:
    
    mic=sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)



    Commande = r.recognize_google(audio, language = "en-US")
    print("Analizying...")
    if(Commande == "send SMS"):
        SMS()
    elif(Commande == "emergency"):
        emergency()
    elif(Commande == "Wikipedia"):
        Wikipedia()
    elif(Commande == "stop"):
        break
