#include <SharpIR.h>

const int trigPin1 = 2;
const int echoPin1 = 3;

const int trigPin2 = 4;
const int echoPin2 = 5;

const int trigPin3 = 6;
const int echoPin3 = 7;

const int Vibra1=40;
const int GND_vibra1=50;

const int Vibra2=41;
const int GND_vibra2=52;

const int Vibra3=42;
const int GND_vibra3=52;

const int VCC1=22;
const int GND1=25;

const int VCC2=28;
const int GND2=31;

const int VCC3=28;
const int GND3=31;

long duration1;
int distance1;


String msg_send = "";

SharpIR sensor( SharpIR::GP2Y0A41SK0F, A0 );

///////////////////////////////////////////////////////////////

void setup() {
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT); 

pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);

pinMode(trigPin3, OUTPUT);
pinMode(echoPin3, INPUT);

pinMode(VCC1, OUTPUT);
pinMode(GND1, OUTPUT);

pinMode(VCC2, OUTPUT);
pinMode(GND2, OUTPUT);

pinMode(VCC3, OUTPUT);
pinMode(GND3, OUTPUT);

pinMode(GND_vibra1, OUTPUT);
pinMode(GND_vibra2, OUTPUT);
pinMode(GND_vibra3, OUTPUT);

pinMode(Vibra1, OUTPUT);
pinMode(Vibra2, OUTPUT);
pinMode(Vibra3, OUTPUT);

Serial.begin(9600); // Starts the serial communication
}

///////////////////////////////////////////////////////////////

void loop() {

digitalWrite(VCC1, HIGH);
digitalWrite(VCC2, HIGH);
digitalWrite(VCC3, HIGH);
digitalWrite(GND1, LOW);
digitalWrite(GND2, LOW);
digitalWrite(GND3, LOW);
digitalWrite(GND_vibra1, LOW);
digitalWrite(GND_vibra2, LOW);
digitalWrite(GND_vibra3, LOW);

measureDist(trigPin1,echoPin1,Vibra1);
measureDist(trigPin2,echoPin2,Vibra2);
measureDist(trigPin3,echoPin3,Vibra3);
Serial.write(msg_send);

}


///////////////////////////////////////////////////////////////
int measureDist(int triggerPin, int echoPin,int motorPin){
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance1= duration*0.034/2;
    if(distance1<30){
      msg_send+='L';
      motorStatus(motorPin,"on");
    }
    else{
      msg_send+='B';
      motorStatus(motorPin,"off");
    }
}

///////////////////////////////////////////////////////////////

void motorStatus(int motorPin, String cmd){
  if(cmd == "on"){
    digitalWrite(motorPin,HIGH);
  }
  else if (cmd == "off"){
    digitalWrite(motorPin,LOW);
  }
}

///////////////////////////////////////////////////////////////

void irDist(int irPin,int motorPin){
  int distance = sensor.getDistance();
  if(distance1<30){
        msg_send+='L';
        motorStatus(motorPin,"on");
      }
       else{
        msg_send+='B';
        motorStatus(motorPin,"off");
      }
}
