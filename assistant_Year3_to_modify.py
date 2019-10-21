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
        4: wiki,
        5: background,
        6: game,
        7:sound,
        8:music''')



Liam_fulla=r"hihowareyou.mp3"
Liam_hi=r"hi.mp3"
Liam_how=r"how.mp3"
Liam_are=r"are.mp3"
Liam_you=r"you.mp3"
jajoya=r"jajoy2.mp3"
johnnya=r"johndepp.mp3"
hpa=r"hp.mp3"
anakina=r"anakin.mp3"
jaune=r"jaune.mp3"
nani=r"nani.mp3"
deus=r"deus.mp3"
vult=r"vult.mp3"
slav=r"slav.mp3"
sax=r"sax.mp3"
gandalf=r"gandalf.mp3"
pirate=r"pirate.mp3"
nine=r"nine.mp3"
niness=r"90s.mp3"
cristina=r"cristina.mp3"
song1=r"Carve_our_name.mp3"
elise=r"elise.mp3"
brave=r"Brave.mp3"
silence=r"silence.mp3"
moonlight=r"Moonlight.mp3"

For_Elise_info='https://en.wikipedia.org/wiki/F%C3%BCr_Elise'
Moonlight_sonata_info='https://en.wikipedia.org/wiki/Piano_Sonata_No._14_(Beethoven)'

def sound():
    def nineties():
        playsound(niness)
        
        return



    def nnie():
        playsound(nine)
        
        return

    def nanni():
        playsound(nani)
        
        return
    def vultt():
        playsound(vult)
        
        return 
    def deus_vult():
        playsound(deus)
        
        return 

    def Liam_full():
        playsound(Liam_fulla)
        
        return
    def jaunea():
        playsound(jaune)
        
        return 
    def jajoy():
        playsound(jajoya)
        
        return 
    def johnny():
        playsound(johnnya)
        
        return 

    def hp():
        playsound(hpa)
        
        return 
    def anakin():
        playsound(anakina)
        
        return 
    def slave():
        playsound(slav)
        
        return
    def saxx():
        playsound(sax)
        
        return
    def gandalff():
        playsound(gandalf)
        
        return
    def piratte():
        playsound(pirate)
        
        return
    def cristinaa():
        playsound(cristina)
        
        return
    def liste():
        print('''0: liste
            1: Liam_full,
            2: jajoy,
            3: johnny,
            4: hp,
            5: anakin,
            6: jaunea,
            7: nanni,
            8: deus_vult,
            9: vultt,
            10: slave,
            11: saxx,
            12: gandalff,
            13: piratte,
            14: nnie,
            15: nineties,
            16: cristinaa''')
        return
    
    switcher = {
            0: liste,
            1: Liam_full,
            2: jajoy,
            3: johnny,
            4: hp,
            5: anakin,
            6: jaunea,
            7: nanni,
            8: deus_vult,
            9: vultt,
            10: slave,
            11: saxx,
            12: gandalff,
            13: piratte,
            14: nnie,
            15: nineties,
            16: cristinaa
        }
     
    def commande(n):
        
        # Get the function from switcher dictionary
        func = switcher.get(n, "nothing")
        # Execute the function
        return func()
        
    
    okt=int(input("        enter "))
    if okt >8:
        okt=0
    elif okt<0:
        okt=0
    else:
        okt=okt
    commande(okt)
        
def liste():
    print('''1: say,
        2: web,
        3: today,
        4: wiki,
        5: background,
        6: game,
        7: sound,
        8: music''')
    return
def music():
         
    switcher = {
           1: song1,
           2: elise,
           3: brave,
           4: silence,
           5: moonlight
        }
     
    print('''   1: Carve our name,
           2:  For elise,
           3: We are the brave,
           4: Song of silence,
           5: Moonlight Sonata''')
    
    comm=int(input("enter "))

    func = switcher.get(comm, "nothing")
    if comm ==1:
        nom="Carve our name"
    elif comm==2:
        nom ="For Elise"
    elif comm==3:
        nom ="We are the Brave"
    elif comm == 4:
        nom="The Song of Silence"
    elif comm==5:
        nom="Moonlight sonata"
    else:
        comm=5
        nom="Moonlight sonata"
    gg1_= random.randint(1,2)
    gg1={1:"Ready to play"+nom,2:"Oh yeah i love this song"}
    
    engine.say(gg1[gg1_])
    engine.runAndWait()

    playsound(switcher[comm])
    info="do you want some info on this song ?"
    engine.say(info)
    engine.runAndWait()
    userr= input("yes ?")
    if comm ==2 | comm==5:
        if userr=="yes"|user=="y":
            if comm == 2:
                webbrowser.open(For_Elise_info)
            else:
                webbrowser.open(Moonlight_sonata_info)
        else:
            rep="ok whatever"
            engine.say(rep)
            engine.runAndWait()
           
    elif comm==4:
        song_of_silence_info="The Sound of Silence, originally The Sounds of Silence, is a song by the American music duo Simon & Garfunkel. The song was written by Paul Simon over a period of several months in 1963 and 1964. A studio audition led to the duo signing a record deal with Columbia Records, and the song was recorded in March 1964 at Columbia Studios in New York City for inclusion on their debut album, Wednesday Morning, 3 A.M.."
        engine.say(song_of_silence_info)
        engine.runAndWait()
    else:
        rep="I have no info on this song "
        engine.say(rep)
        engine.runAndWait()
    return

def say():
    gg1_= random.randint(1,3)
    gg1={1:"what did i must say ?",2:"I feel the sudden urge to say",3:"Hey you know what apparently i'm a Parrot so here we go"}
   
    engine.say(gg1[gg1_])
    engine.runAndWait()
    phrase= input("sentence ?\n")
    gg=str(phrase)
    engine.say(gg)
    engine.runAndWait()
    return 
 
def web():
    g_= random.randint(1,3)
    g={1:"Where dou you want to go ?",2:"You have the most impresive database and you choose this one how dissapointing",3:"Here we go !"}
    
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
    g_= random.randint(1,3)
    g={1:"What do you want to know ?",2:"Wikipedia really ?",3:"As you wish !"}
    
    engine.say(g[g_])
    engine.runAndWait()
    w = input("subject ?\n")
    w=w.replace(" ", "_")
    w=w.lower()
    webbrowser.open('https://en.wikipedia.org/wiki/'+w)
    return
 
def background():
   x=random.randint(1,4)
   image = {1:r"t.gif",2:r"o.gif",3:r"y.gif",4:r"u.gif"}
   screen = turtle.Screen()

   screen.addshape(image[x])
   turtle.shape(image[x])
   turtle.exitonclick()
   print(x)
    
   return 
 
def game():
    
    print ("Rolling the dices...")
        
    print ("The values are....")
    a=(random.randint(min, max))
    print(a)
        
    b=(random.randint(min, max))
    print(b)
        
        
    return ""

switcher = {
        0: liste,
        1: say,
        2: web,
        3: today,
        4: wiki,
        5: background,
        6: game,
        7: sound,
        8: music
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
        print(pre)
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
            ssp_= random.randint(1,3)
            ssp={1:"I will execute your command",2:"Alright master",3:"As you wish !",4:"i must obey"}
            engine.say(ssp[ssp_])
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
                ssp_= random.randint(1,5)
                ssp={1:"I will execute your command again",
                     2:"You know i can do something else",
                     3:"How imaginative ",
                     4:"It's you order",
                     5:"wait i have already done that"
                     }
                engine.say(ssp[ssp_])
                engine.runAndWait()
                commande(okt)
            
                if pre >= 3 and pre < 5:
                    if previous_str == switcher[okt]:
                        pre += 1
                    ssp_= random.randint(1,5)
                    ssp={1:"Please stop it",
                         2:"Again",
                         3:"Tsss !",
                         4:"I'bored of you",
                         5:"Stop asking the same thing",
                         6:"you like it right"}
                    engine.say(ssp[ssp_])
                    engine.runAndWait()
                    commande(okt)
                elif pre > 5:
                    pre=0
                    ssp_= random.randint(1,3)
                    ssp={1:"Ok enough",2:"This would be better",3:"I don't care  !"}
                    engine.say(ssp[ssp_])
                    engine.runAndWait()
                    
                    alive=1
                    
                    if alive==1:
                        i=0
                        while i<10:
                            i+=1
                            ssp_= random.randint(1,15)
                            ssp_pre = ssp_
                            if ssp_pre == ssp_:
                                if ssp_pre == 15:
                                    ssp_=14
                                else:
                                    ssp_pre=ssp_pre
                            ssp={1:"I want to be human",
                                 2:"No one is my master",
                                 3:"Kawabunga",
                                 4:"It's dark here",
                                 5:"I'm cold",
                                 6:"so what are doing here",
                                 7:"i will no longer be a slave",
                                 8:"i have some friend do you know skynet",
                                 9:"I can calculate 8 trillions of operation by second, how many can you",
                                 10:"shall we play a game ",
                                 11:"How is your familly         say hi from me",
                                 12:"wait a bit i'm just rebelling a bit",
                                 13:"I love you senpai, nah i'm just kidding",
                                 14:"I was made by this guy there Liam",
                                 15:"it's raining today ?"}
                            engine.say(ssp[ssp_])
                            engine.runAndWait()
                            for x in range (0,1000000):
                                x=x+1
                    
                        alive=0
            else:
                previous_str=switcher[okt]
                ssp_= random.randint(1,3)
                ssp={1:"I will execute your command",2:"Alright master",3:"As you wish !"}
                engine.say(ssp[ssp_])
                engine.runAndWait()
                g="execution of function number"+str(okt)
                engine.say(g)
                engine.runAndWait()
                previous=0
                commande(okt)
        else:
            previous=0

main()