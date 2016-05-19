import RPi.GPIO as GPIO
import time
import sys
import os
from rssi import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(16,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(0)
s2.start(0)

#s1_speed = 7.0
#s2_speed = 7.0

def circle(turn_time):
    # while True:
    # doable: s1 = 7.9, s2 = 6.6
    s1_speed = 7.8
    s1.ChangeFrequency(50 - (0.5 * s1_speed))
    s1.ChangeDutyCycle(s1_speed)

    s2_speed = 6.7
    s2.ChangeFrequency(50 - (0.5 * s2_speed))
    s2.ChangeDutyCycle(s2_speed)
    time.sleep(turn_time)
    s1.start(0)
    s2.start(0)
    
    
def circle_rssi():
    while True:
        # doable: s1 = 7.7, s2 = 6.6
        s1_speed = 7.9
        s1.ChangeFrequency(50 - (0.5 * s1_speed))
        s1.ChangeDutyCycle(s1_speed)

        s2_speed = 6.5
        s2.ChangeFrequency(50 - (0.5 * s2_speed))
        s2.ChangeDutyCycle(s2_speed)
        rssimean()
        
    
circle(40)        


