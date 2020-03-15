################################################################ Variables & Import

import os,random
import webbrowser
import datetime
import turtle
import math
import random
import requests
from twilio.rest import Client
import serial
import pyttsx3
engine = pyttsx3.init()
min = 1
max = 6
i=1

account_sid ="XXX" # Put your Twilio account SID here

auth_token ="XXX" # Put your auth token here


Number_list = ["+","+tel"]

list_detect = ['N','N','N','N','N','N','N','N']
count = 0
send_data=""
arduino = serial.Serial('COM1', 9600, timeout=.1)

################################################################## Main Code
start_= random.randint(1,3)
start={1:"Hi !",2:"Hello, How are you ?",3:"Greetings"}
engine.say(start[start_])
engine.runAndWait()
now = datetime.datetime.now()

print('''1: send a S_M_S,
2: web,
3: today,
4: wiki,
5: Emergency
6: Detection
        ''')





 
   
def liste():
    print('''1: send a S_M_S,
2: web,
3: today,
4: wiki,
5: Emergency,
6: Detection
        ''')
    print(list_detect)
    return

def Serial_reading_():
    count=0
    while(count<10):
        
        string_answer_from_serial = arduino.read(10)
        if b'O' in string_answer_from_serial:
            print("Detection")
            send_data= "O"
            sensor_id=[pos for pos, char in enumerate(string_answer_from_serial) if char == send_data]
            print("Id  of the sensor who have a detection",sensor_id)
            list_detect[count] = 'O'
           
        else:
            print("No Detection")
            send_data= "N"
            list_detect[count] = 'P'
        count=count+1
        
        return list_detect

def SMS():
    
   
    engine.say("What is the message")
    engine.runAndWait()
    phrase= input("sentence ?\n")
    gg=str(phrase)
    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+447588675953", # Put your Twilio number here

        body="This is a message send to you via the Smart Jacket -->"+gg)
    

    return 
 
def web():
    
    g={1:"Type in a web page"}
    
    engine.say(g[1])
    engine.runAndWait()
    w = input("address ?\n")
    return webbrowser.open('http://'+w+'.ie')
 
def today():
    day = datetime.date.today().strftime('%A')
    month = datetime.date.today().strftime('%B')
    date = datetime.date.today().strftime('%d')
    g="Today is"+day+date+month
    engine.say(g)
    engine.runAndWait()
    return str(now)
 
def wiki():
    
    g={1:"What do you want to know ?"}
    
    engine.say(g[1])
    engine.runAndWait()
    w = input("subject ?\n")
    w=w.replace(" ", "_")
    w=w.lower()
    webbrowser.open('https://en.wikipedia.org/wiki/'+w)
    return
def emergency():
    def display_position():
        """  Function To Print GeoIP Latitude & Longitude """
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
        geo_data = geo_request.json()
        
        a=("latitude "+geo_data['latitude'],"longitude "+geo_data['longitude'],geo_data['city'],geo_data['region'],geo_data['country'])
       
        str =  ' --   '.join(a) 
        return str

   

    client = Client(account_sid, auth_token)
    for i in Number_list:


        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+447588675953", # Put your Twilio number here

        body="Jacket alert system press SEND EMERGENCY COORDONATE : --   "+display_position())
    return



     

switcher = {
        0: liste,
        1: SMS,
        2: web,
        3: today,
        4: wiki,
        5: emergency,
        6:Serial_reading_
        
    }
 
def commande(n):
    
    # Get the function from switcher dictionary
    func = switcher.get(n, "nothing")
    # Execute the function
    return func()





def main():    
    alive=0
    u=0
    o=1
    pre =0
    previous=0
    while u!=o:
        
        if previous==0:
            okt=int(input("enter "))
            if okt >8:
                okt=0
            elif okt<0:
                okt=0
            else:
                okt=okt
            previous=1
            previous_str=switcher[okt]
            engine.say("I will execute your command")
            engine.runAndWait()
            commande(okt)
        elif previous == 1 :
            okt=int(input("enter "))
            if okt >8:
                okt=0
            elif okt<0:
                okt=0
            else:
                okt=okt
            if previous_str == switcher[okt]:
                pre += 1
                
                engine.say("I will execute the same command again")
                engine.runAndWait()
                commande(okt)
            
                if pre >= 3 and pre < 5:
                    if previous_str == switcher[okt]:
                        pre += 1
                    
                    engine.say("And again")
                    engine.runAndWait()
                    commande(okt)
                
            else:
                previous_str=switcher[okt]
                engine.say("I will execute your command")
                engine.runAndWait()
                g="execution of function number"+str(okt)
                engine.say(g)
                engine.runAndWait()
                previous=0
                commande(okt)
        else:
            previous=0




















main()
