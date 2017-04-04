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
       throttle.write(78);
       steering.write(70);
       //usbRead = 0; 
     }  
     else if(usbRead == 'c'){
       throttle.write(90);
       steering.write(109);
     }
     else if(usbRead == 'd'){
      throttle.write(83);
      steering.write(109);
     }
     else if(usbRead == 'b'){
      throttle.write(82);
      steering.write(130);
     }
     //delay(1000);
   } //end of serial.available
   
   //else{
     //throttle.write(90);
   //}
   
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
