import RPi.GPIO as GPIO
import time
import sys
import os
from rssi import *
from face import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(16,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(0)
s2.start(0)

TURN_TIME = 10

def run_arc(turn_time):
    s1_speed = 7.9
    s1.ChangeFrequency(50 - 0.5 * s1_speed)
    s1.ChangeDutyCycle(s1_speed)

    s2_speed = 6.6
    s2.ChangeFrequency(50 - 0.5 * s2_speed)
    s2.ChangeDutyCycle(s2_speed)
    time.sleep(turn_time)

def pause():
    s1.start(0)
    s2.start(0)

def circle():
    rssi_max = -1000
    count = 0
    circle_list = {}
    print "--------------first round----------------"
    while count < 4:
        print "----------count: %d" %(count)
        print "calculating"
        rssi_mean = rssimean()
        if rssi_mean != 0:
            circle_list[count] = rssi_mean
            print "key: %d, value: %f" %(count, rssi_mean)

        run_arc(TURN_TIME)
        pause()
        count += 1
    
    # replace the first value in the list
    rssi_mean = rssimean()
    circle_list[0] = max(circle_list[0], rssi_mean)
        
    # find max rssi
    for k, v in circle_list.items():
        print (k,v)
        if v >= rssi_max:
            rssi_max = v
    count_run = circle_list.keys()[circle_list.values().index(rssi_max)]
    print "rssi_max: %s, count_run: %s" %(rssi_max, count_run) 
    
#    # find the max rssi based on time -- too much deviation
#    i = 1
#    while i < count_run:
#        print "inside while count_run is : %s" %(count_run)
#        print "count is %s" %(count)
#        run_arc(TURN_TIME)
#        i += 1
#        print i
#        s1.start(0)
#        s2.start(0)
#        time.sleep(1)

    print "--------------second round--------------"
#    if count_run != 0:
    rssi = circle_list[0]
    # if the current rssi is less than rssi_max
    while (rssi < rssi_max - 2):
        print "rssi: %s" %(rssi)
        run_arc(TURN_TIME * 1.0 / 2)
        pause()            
        rssi = rssimean()
        
    print "finish second round"
        
    pause() # stops at rssi_max position
    return rssi_max
    

def turn(turning):
    # left rotate for 90 degree
    s1.start(0)
    s2_speed = 6.5
    s2.ChangeFrequency(50 - 0.5 * s2_speed)
    s2.ChangeDutyCycle(s2_speed)
    time.sleep(turning)
    s2.start(0)

def forward(forward_time, rssi_max):
    
    is_found = False
    rssi_prev = rssi_max
    rssi = rssi_prev
    
    print "in forward rssi is %s" %(rssi)
    
    # getting closer but not yet arrived
    while rssi >= rssi_prev and rssi < -65:
        rssi_prev = rssi
        # go straight
        s1_speed = 8
        s1.ChangeFrequency(50 - 0.5 * s1_speed)
        s1.ChangeDutyCycle(s1_speed)
        s2_speed = 6
        s2.ChangeFrequency(50 - 0.5 * s2_speed)
        s2.ChangeDutyCycle(s2_speed)
        time.sleep(forward_time)
        # stop
        pause()
        rssi = rssimean()
        print "current rssi is %s" %(rssi)
       
    # turning to find face
    s1.start(0)
    s2_speed = 6.9
    s2.ChangeFrequency(50 - 0.5 * s2_speed)
    s2.ChangeDutyCycle(s2_speed)

    # if face is found
    if find_face():
        print "find face"
        s2.start(0)
        is_found = True
    else:
        print "fail to find face"
        s2.start(0)
        is_found = False

    return is_found
        
#circle()
