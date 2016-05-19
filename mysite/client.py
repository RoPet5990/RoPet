import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(16,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(0)
s2.start(0)

s1_speed = 7.0
s2_speed = 7.0


def motor_control(cmd):
    global s1_speed
    global s2_speed
    
    if cmd == 'forward':
        s1_speed = 7.3
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        
        s2_speed = 6.7
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        
        print 'forward: s1 is %s, s2 is %s' %(s1_speed, s2_speed)

    if cmd == 'backward':
        s1_speed = 6.7
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        
        s2_speed = 7.3
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
            
        print 'backward: s1 is %s, s2 is %s' %(s1_speed, s2_speed)

    if cmd == 'stop':
        s1.start(0)
        s2.start(0)
        print 'stop: s1 is %s, s2 is %s' %(s1_speed, s2_speed)

    if cmd == 'quit':
        print "quit----"
        s1.start(0)
        s2.start(0)
        GPIO.cleanup()
        
    if cmd == 'resume':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19,GPIO.OUT) #s1 left
        GPIO.setup(26,GPIO.OUT) #s2 right
        #s1 = GPIO.PWM(19,46.5)
        #s2 = GPIO.PWM(26,46.5)
        s1.start(0)
        s2.start(0)
        print 'resume: s1 is %s, s2 is %s' %(s1_speed, s2_speed)
        
    if cmd == 'up':
	if s1_speed == 7.0:
	    s1_speed = 7.1        
	if s2_speed == 7.0:
            s2_speed = 6.9

        if (s1_speed > 7.0 and s1_speed < 8.0):
            s1_speed += 0.1
        elif (s1_speed < 7.0 and s1_speed > 6.0):
            s1_speed -= 0.1
            
        if (s2_speed > 7.0 and s2_speed < 8.0):
            s2_speed += 0.1
        elif (s2_speed < 7.0 and s2_speed > 6.0):
            s2_speed -= 0.1
            
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        print 'up: s1 is %s, s2 is %s' %(s1_speed, s2_speed)
          
    if cmd == 'down':
        
	if s1_speed == 7.0:
            s1_speed = 7.1
        if s2_speed == 7.0:
            s2_speed = 6.9

        if (s1_speed > 7.0 and s1_speed < 8.0):
            s1_speed -= 0.1
        elif (s1_speed < 7.0 and s1_speed > 6.0):
            s1_speed += 0.1
            
        if (s2_speed > 7.0 and s2_speed < 8.0):
            s2_speed -= 0.1
        elif (s2_speed < 7.0 and s2_speed > 6.0):
            s2_speed += 0.1
            
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        print 'down: s1 is %s, s2 is %s' %(s1_speed, s2_speed)
        
    if cmd == 'left':
        s1_speed = 7.2
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        
        s2_speed = 6.5
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
            
        print 'backward: s1 is %s, s2 is %s' %(s1_speed, s2_speed)
        
    if cmd == 'right':
        s1_speed = 7.5
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        
        s2_speed = 6.8
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
            
        print 'backward: s1 is %s, s2 is %s' %(s1_speed, s2_speed)
        
