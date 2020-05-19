import serial
from datetime import datetime
import os

now =datetime.now()

list_detect = ['N','N','N','N','N','N','N']
count = 0
send_data =""
arduino = serial.Serial('COM1',9600,timeout=0.1)
f = open("Save.txt","w+")
f.close()
while(True):
    f = open("Save.txt","a+")
    string_from_serial = arduino.read(10)
    if 'L' in string_from_serial:
        if i ==200:
            if os.path.exists("Save.txt"):
                os.remove("Save.txt")
        TimeStamp = now.strftime("%d/%m/%Y, %H : %M : %S")
        f.write("Time Stamp: "+TimeStamp+" "+list_detect % (i+1))