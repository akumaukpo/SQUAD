#include <Servo.h>
 
 Servo throttle;
 Servo steering;
 
 int pos = 0;
 char usbRead;
 
 void setup(){
   Serial.begin(9600);
   throttle.attach(9);
   steering.attach(10);
   throttle.write(90);
   steering.write(109);
   //delay(5000);
 }
 
 void loop(){
   
   if(Serial.available()){
     usbRead = Serial.read();  
     Serial.println(usbRead);
     if(usbRead == 'a'){
       steering.write(70);
       //usbRead = 0; 
     }  
     else if(usbRead == 'c'){
       throttle.write(90);
     }
     else if(usbRead == 'd'){
      throttle.write(135);
     }
     else if(usbRead == 'b'){
      steering.write(130);
     }
     delay(1000);
   } //end of serial.available
 } //end of loop()
 
 /*
 speed control
   throttle:
     90 = neutral
     80 = forward and slow
     110 = backward and slow
   steering:
     109 = neutral
     80 = slightly right
     130 = slightly left
 */
