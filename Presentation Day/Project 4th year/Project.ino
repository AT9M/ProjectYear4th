 
  #include <SharpIR.h>

const int trigPin1 = 2;
const int echoPin1 = 3;

const int trigPin2 = 4;
const int echoPin2 = 5;

const int trigPin3 = 6;
const int echoPin3 = 7;

const int Vibra1 = 40;
const int GND_vibra1 = 50;

const int Vibra2 = 41;
const int GND_vibra2 = 51;

const int Vibra3 = 42;
const int GND_vibra3 = 52;

const int VCC1 = 22;
const int GND1 = 25;

const int VCC2 = 28;
const int GND2 = 31;

const int VCC3 = 32;
const int GND3 = 34 ;

const int VCC4 = 44;
const int GND4 = 45;

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

  pinMode(VCC4, OUTPUT);
  pinMode(GND4, OUTPUT);

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
  digitalWrite(VCC4, HIGH);
  digitalWrite(GND1, LOW);
  digitalWrite(GND2, LOW);
  digitalWrite(GND3, LOW);
  digitalWrite(GND4, LOW);
  digitalWrite(GND_vibra1, LOW);
  digitalWrite(GND_vibra2, LOW);
  digitalWrite(GND_vibra3, LOW);

measureDist(trigPin1,echoPin1,Vibra1);


measureDist(trigPin3,echoPin3,Vibra2);

irDist();

}


///////////////////////////////////////////////////////////////
int measureDist(int triggerPin, int echoPin, int motorPin) {
  long duration1;
  int distance1;
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  duration1 = pulseIn(echoPin, HIGH);
  distance1= duration1*0.034/2;
    if(distance1<=30){
      digitalWrite(motorPin, HIGH);
      delay(250);
      digitalWrite(motorPin, LOW);
      
      msg_send+='L';
    }
    else{
      msg_send+='B';
      
    }
}

///////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////

int irDist() {
  int distance2 = sensor.getDistance();
  if (distance2 <= 3) {
    
    digitalWrite(Vibra3, HIGH);
    delayMicroseconds(150);
    digitalWrite(Vibra3, LOW);
    msg_send += 'L';
  }
  else {
    
    digitalWrite(Vibra3, LOW);
    msg_send += 'B';
  }
  Serial.println(distance2);
  return distance2;

}
