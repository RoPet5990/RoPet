import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right


GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP) #plus
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP) #minus
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)

s1=GPIO.PWM(19,50)
s2=GPIO.PWM(26,50)

s2.start(0)

s2.ChangeDutyCycle(7.0)

speed = 7.0
freq = 46.5

def GPIO22_left(channel):
    global speed
    global freq
    speed += 0.1
    freq = 50 - 0.5 * speed
    s2.ChangeFrequency(freq)
    s2.ChangeDutyCycle(speed)
    print 's1 is %s' %(speed)
    
def GPIO23_left(channel):
    global speed
    global freq
    speed -= 0.1
    freq = 50 - 0.5 * speed
    s2.ChangeFrequency(freq)
    s2.ChangeDutyCycle(speed)
    print 's1 is %s' %(speed)

def GPIO17_leftStop(channel):
    sys.exit()

GPIO.add_event_detect(17,GPIO.FALLING,callback=GPIO17_leftStop,bouncetime=200)

GPIO.add_event_detect(22,GPIO.FALLING,callback=GPIO22_left,bouncetime=200)
GPIO.add_event_detect(23,GPIO.FALLING,callback=GPIO23_left,bouncetime=200)

while 1:
    time.sleep(0.1)
