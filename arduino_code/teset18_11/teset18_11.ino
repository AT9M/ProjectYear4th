

int incoming_state =0;
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
pinMode(LED_BUILTIN, OUTPUT);
Serial.begin(9600); // Starts the serial communication

}
void loop() {


  Ultra(3,2,1);
   Ultra(5,4,2);
  if (Serial.available() > 0){  //Looking for incoming data
      //Reading the data
     if(Serial.read()=='O1'){
          //contact vibrate motor 01
             
       }
       else if(Serial.read()=='O2')
       {
         //contact vibrate motor 02
       }
      //Making the LED light up or down
  }
}
void Ultra(const int pintrigger ,const int echopin, int numb){
  digitalWrite(pintrigger, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(pintrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pintrigger, LOW);
  duration = pulseIn(echopin, HIGH);
  distance= duration*0.034/2;
  //Serial.println(distance);
  if(distance < 80){
  thisString = "O";
  }
  else{
  thisString="N";
  } 
  Serial.write(numb);
  Serial.print(thisString);
  Serial.println();
}
