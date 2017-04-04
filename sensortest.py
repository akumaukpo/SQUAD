#! /usr/bin/env python
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO2
import RPi.GPIO as GPIO3
import time

import serial


usbCom = serial.Serial("/dev/ttyACM0", 9600)
##usbCom.open()
while True:

    GPIO.setmode(GPIO.BCM)

    TRIG=18 ##middle sensor
    ECHO=17

    print "distance measurement in progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


    GPIO.output(TRIG,False)
    
    time.sleep(.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    print"1"

    while GPIO.input(ECHO)==0:
        start = time.time()
    print"a"
    while GPIO.input(ECHO)==1:
        end = time.time()
    print"b"

    pulse_duration = end - start
    distance = pulse_duration * 17150
    distance = distance / 2.54
    distance = round (distance,2)
    print "distance:", distance , "inches"


    GPIO3.setmode(GPIO3.BCM)
    GPIO2.setmode(GPIO2.BCM)

    TRIG=16
    ECHO=19
    TRIG2=23
    ECHO2=22

       

    GPIO3.setup(TRIG,GPIO3.OUT)
    GPIO3.setup(ECHO,GPIO3.IN)



    GPIO3.output(TRIG,False)

    time.sleep(.1)

    GPIO3.output(TRIG, True)


    time.sleep(0.00001)
    GPIO3.output(TRIG, False)

    print"2"

    while GPIO3.input(ECHO)==0:
        pulse_start = time.time()
    print"s"
    while GPIO3.input(ECHO)==1:
        pulse_end = time.time()
    print"r"
    pulse_duration = pulse_end - pulse_start
    distance3 = pulse_duration * 17150
    distance3 = distance3 / 2.54
    distance3 = round (distance3,2)
    print "distance:", distance3 , "inches"

    GPIO2.setup(TRIG2,GPIO2.OUT)
    GPIO2.setup(ECHO2,GPIO2.IN)
    
    GPIO2.output(TRIG2,False)
    
    time.sleep(.1)

    GPIO2.output(TRIG2, True)

    time.sleep(0.00001)

    GPIO2.output(TRIG2, False)


    while GPIO2.input(ECHO2)==0:
        pulse_start = time.time()
    print "x"
    while GPIO2.input(ECHO2)==1:
        pulse_end = time.time()
    print "y"


    pulse_duration = pulse_end - pulse_start
    distance2 = pulse_duration * 17150
    distance2 = distance2 / 2.54
    distance2 = round (distance2,2)
    print "distance2:", distance2 , "inches"

    if (distance3 > distance2) and (distance < 25) :
        usbCom.write('a')
        time.sleep(2)
    elif (distance3 < distance2) and (distance < 25) :
        usbCom.write('b')
        time.sleep(2)
    elif (distance3 > distance2) and (distance2 < 20):
        usbCom.write('e')
    elif (distance3 < distance2) and (distance3 < 20) :
        usbCom.write('f')
        time.sleep(2)
    elif (distance3 and distance2 and distance < 10):
        usbCom.write('c')
    
    else :
        usbCom.write('d')

    

    GPIO.cleanup()    
    GPIO2.cleanup()
    GPIO3.cleanup()   


