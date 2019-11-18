const int trigPin = 3;
const int echoPin = 2;
const int trigPin2 = 5;
const int echoPin2 = 4;
// defines variables
long duration;
int distance;
String thisString ;
const byte numChars = 32;
char receivedChars[numChars]; // an array to store the received data

boolean newData = false;



void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(trigPin2, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin2, INPUT);
Serial.begin(9600); // Starts the serial communication

}
void loop() {

for(int i=0;i<2;i++){
  Ultra(2,3,1);
}
}

void Ultra(int i ,int j, int numb){
  digitalWrite(i, LOW);
  delayMicroseconds(2);
  digitalWrite(i, HIGH);
  delayMicroseconds(10);
  digitalWrite(i, LOW);
  duration = pulseIn(j, HIGH);
  distance= duration*0.034/2;
  if(distance > 80){
  thisString = numb+"N";
  }
  else{
  thisString= numb+"O";
  } 
  Serial.write("");
  Serial.println(thisString);
}
