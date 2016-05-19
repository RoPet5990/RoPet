import RPi.GPIO as GPIO
import time
import sys
import os
from rssi import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(19,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(0)
s2.start(0)

s1_speed = 7.0
s2_speed = 7.0


def line(turn_time):
    rssi_max = -1000
    count = 0
    circle_list = {}
    print "first time"
    while count < 8:
        rssi_mean = rssimean()
        if rssi_mean != 0:
            circle_list[count] = rssi_mean
            print "key is %s, value is %s" %(str(count), str(rssi_mean))
        print "====start==="
        print "count is %d" %(count)
        # run for an arc
        s1_speed = 8
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)

        s2_speed = 6
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        time.sleep(turn_time)
        
        # stop and calculate rssi_mean
        print "**stop**"
        s1.start(0)
        s2.start(0)
        count += 1
        
    # find max rssi
    print "--------------second round--------------"
    for k, v in circle_list.items():
        print "---"
        print (k,v)
        if v >= rssi_max:
            rssi_max = v
    print "rssi_max is : %s" %(rssi_max) 
    count_run = circle_list.keys()[circle_list.values().index(rssi_max)]
    print "count_run is : %s" %(count_run)
    
    i = 1
    while i < count_run:
        print "inside while count_run is : %s" %(count_run)
        print "count is %s" %(count)
        s1_speed = 6
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)

        s2_speed = 8
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        time.sleep(turn_time)
        i += 1
        print i
    print "finish second round"
        
    s1.start(0)
    s2.start(0)

    return rssi_max

line(3)