#include <Servo.h> 
 
Servo throttle;  // create servo object to control the motor of the car 
Servo steering;  // create servo object to control the steering of the car
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  throttle.attach(9);  // attaches the servo object to pin 9 of the Arduino
  steering.attach(10); // attaches the servo object to pin 10 of the Arduino
  throttle.write(90);
  steering.write(109);
  delay(5000);
} 
 
void loop() 
{ 
                             
    throttle.write(79);  
    //steering.write(109);
    delay(5500);
    throttle.write(118);
    //steering.write(79);
    delay(5500);
    throttle.write(65);
    steering.write(65);
    delay(7500);
    throttle.write(80);
    steering.write(109);
    delay(4500);
    throttle.write(165);
    steering.write(140);
    delay(6500);
    throttle.write(82);
    steering.write(109);
    delay(5000);
    throttle.write(65);
    steering.write(150);
    delay(8000);
    steering.write(90);
    delay(20000);

} 

/*
speed control:
  throttle:
    90 = neutral
    85 = forward slow pace
    110 = backward slow pace
    
  steering:
    109 = neutral (trying to compensate for misallignment)
    80 = slight right turn
    130 = slight left turn

*/

