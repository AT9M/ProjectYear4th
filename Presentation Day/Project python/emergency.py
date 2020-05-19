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

        to=str(i), # Put your cellphone number here

        from_="+447588675953", # Put your Twilio number here

        body="Jacket alert system SEND LAST COORDONATE : --   "+display_position())
    return
