from pygame import mixer
import os,random
import webbrowser
import datetime
import turtle
import math
import random
import pyttsx3
engine = pyttsx3.init()
min = 1
max = 6
i=1
from playsound import playsound




start_= random.randint(1,3)
start={1:"Hi !",2:"Hello, How are you ?",3:"Greetings"}
engine.say(start[start_])
engine.runAndWait()
now = datetime.datetime.now()

print('''   1: say,
        2: web,
        3: today,
        4: wiki
        ''')





 
   
def liste():
    print('''   1: send a S_M_S,
                2: web,
                3: today,
                4: wiki''')
    return

def say():
    
   
    engine.say("What is the message")
    engine.runAndWait()
    phrase= input("sentence ?\n")
    gg=str(phrase)
    engine.say(gg)
    engine.runAndWait()
    return 
 
def web():
    g_= random.randint(1,2)
    g={1:"Where dou you want to go ?",2:"Here we go !"}
    
    engine.say(g[g_])
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
    g_= random.randint(1,2)
    g={1:"What do you want to know ?",3:"As you wish !"}
    
    engine.say(g[g_])
    engine.runAndWait()
    w = input("subject ?\n")
    w=w.replace(" ", "_")
    w=w.lower()
    webbrowser.open('https://en.wikipedia.org/wiki/'+w)
    return

 

switcher = {
        0: liste,
        1: say,
        2: web,
        3: today,
        4: wiki,
        
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