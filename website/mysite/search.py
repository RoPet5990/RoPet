import RPi.GPIO as GPIO
import time
import sys
import os
from rssi import *
from camera_control import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #s1 left
GPIO.setup(26,GPIO.OUT) #s2 right
s1 = GPIO.PWM(16,46.5)
s2 = GPIO.PWM(26,46.5)
s1.start(0)
s2.start(0)

TURN_TIME = 10

def run_arc(turn_time):
    s1_speed = 7.8
    s1.ChangeFrequency(50 - 0.5 * s1_speed)
    s1.ChangeDutyCycle(s1_speed)

    s2_speed = 6.7
    s2.ChangeFrequency(50 - 0.5 * s2_speed)
    s2.ChangeDutyCycle(s2_speed)
    time.sleep(turn_time)

def pause():
    s1.start(0)
    s2.start(0)

def turn_and_find():
    camera = CameraControl()
    is_found = False
    s1.start(0)
    s2_speed = 6.9
    s2.ChangeFrequency(50 - 0.5 * s2_speed)
    s2.ChangeDutyCycle(s2_speed)

    # if face is found
    if camera.find_face():
        print "find face"
        is_found = True
    else:
        print "fail to find face"
        is_found = False
    # turn off camera here
    camera.close()
    s2.start(0)
    return is_found

def circle(is_found):
    rssi_max = -1000
    count = 0
    circle_list = {}
    print "-------------- FIRST ROUND ----------------"
    while count < 6:
        print "Arc No.%d" %(count)
        print "Calculating mean rssi at this position......"
        rssi_mean = rssimean()
        if rssi_mean != 0:
            circle_list[count] = rssi_mean
            print "Arc No.%d, rssi: %f" %(count, rssi_mean)

            # if find the face then break
            if rssi_mean > -63 and turn_and_find():
                is_found = True
                return 

        run_arc(TURN_TIME)
        pause()
        count += 1
    
    # # replace the first value in the list
    # rssi_mean = rssimean()
    # circle_list[0] = max(circle_list[0], rssi_mean)
        
    # find max rssi
    for k, v in circle_list.items():
        print (k,v)
        if v >= rssi_max:
            rssi_max = v
    # the number of arc where we got the maximum rssi
    count_run = circle_list.keys()[circle_list.values().index(rssi_max)]
    print "TESTING..rssi_max: %s, count_run: %s" %(rssi_max, count_run) 

    print "-------------- SECOND ROUND ----------------"
    rssi = circle_list[0]
    # if the current rssi is less than rssi_max, keep running arcs
    while (rssi < rssi_max - 2):
        print "rssi: %s" %(rssi)
        run_arc(TURN_TIME * 1.0 / 2)    # running a smaller arc
        pause()            
        rssi = rssimean()
        
    print "-------------- SECOND ROUND FINISHED! ----------------"
        
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
    
    rssi_prev = rssi_max
    rssi = rssi_prev
    
    print "The current rssi is %s" %(rssi)
    
    # getting closer but not yet arrived
    while rssi >= rssi_prev and rssi < -63:
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
    return turn_and_find()
