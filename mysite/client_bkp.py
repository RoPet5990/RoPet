import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(19,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(7)
s2.start(7)

def motor_control(cmd):
    if cmd == 'forward':
        s1.ChangeFrequency(50)
        s1.ChangeDutyCycle(8.0)
        s2.ChangeFrequency(50)
        s2.ChangeDutyCycle(6.0)
        print 'forward'

    if cmd == 'backward':
        s1.ChangeFrequency(50)
        s1.ChangeDutyCycle(6.0)
        s2.ChangeFrequency(50)
        s2.ChangeDutyCycle(8.0)
        print 'backward'

    if cmd == 'stop':
        s1.ChangeFrequency(50)
        s1.ChangeDutyCycle(0)
        s2.ChangeFrequency(50)
        s2.ChangeDutyCycle(0)
        print 'stop'

    if cmd == 'quit':
        s1.start(0)
        s2.start(0)
        GPIO.cleanup()

    if cmd == 'resume':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19,GPIO.OUT) #s1 left
        GPIO.setup(26,GPIO.OUT) #s2 right
        #s1 = GPIO.PWM(19,50)
        #s2 = GPIO.PWM(26,50)
        s1.start(0)
        s2.start(0)
        print 'resume'

