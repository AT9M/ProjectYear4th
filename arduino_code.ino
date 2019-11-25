String DetectionValueUltra[8] = {'N','N','N','N','N','N','N','N'};
String Vibration_motor[8] = {'P','P','P','P','P','P','P','P'};
String DetectionValueIR[2] = {'N','N'};
void setup() {
  // put your setup code here, to run once:
//different snsor input and output
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(sensor, LOW);//clear
delayMicroseconds(2);

digitalWrite(sensor, HIGH);   //add the other for ultrasonic
delayMicroseconds(10);
digitalWrite(sensor, LOW);

for(int j =0;j<=8;j++){
Detec_Ultrason(sensor_echopin,j)   //sensor_echopin = echo pin on the HR SO4 and j the id number of the sensor
}
for(int k =0;k<=2;k++){
Detect_IR(sensor,k)   //sensor_echopin = echo pin on the HR SO4 and j the id number of the sensor
}

}

String Detec_Ultrason(sensor_echopin, int i){
  int times = millis()
          duration = pulseIn(sensor_echopin, HIGH);
          // Calculating the distance
          distance= duration*0.034/2;
          // Prints the distance on the Serial Monitor
          if(distance<80){
            DetectionValueUltra[i]='O';
            if((times - 1000) >= 0){Vibrate(vibra_pin);times =0;}
            Stop_vibrate(vibra_pin)
          }
          else{
           DetectionValueUltra[i]='N';
           Stop_vibrate(vibra_pin)
          }

          return Serial.println(DetectionValueUltra[i]);
}


String Detect_IR(sensor, int i){
          float volts = analogRead(sensor)*0.0048828125;  // value from sensor * (5/1024)
          int distance = 13*pow(volts, -1);
         
          if(distance<30){
            DetectionValueIR[i]='O';
           if((times - 1000) >= 0){Vibrate(vibra_pin);times =0;}
            Stop_vibrate(vibra_pin)
          }
          else{
           DetectionValueIR[i]='N';
           Stop_vibrate(vibra_pin)
          }

          return Serial.println(DetectionValueIR[i]);
}

void Vibrate(int i){
  digitalWrite(i,HIGH);
}
void Stop_vibrate(int i){
  digitalWrite(i,LOW);
}
