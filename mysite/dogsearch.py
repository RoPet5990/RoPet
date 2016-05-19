import time
from rssi import *
from search import *
from camera_control import *
    
def dogsearch():
    state = "ready"
    prev_rssi = 0
    rssi = 0
    is_found = False
    while True:
        # get origin rssi
        print "=========== CURRENT STATE: %s===========" %(state)
        prev_rssi = rssi
        if state == "ready":
            rssi = rssimean()
            state = "wait"

        elif state == "wait":
            rssi = rssimean()
            print "Previous rssi was: %s" %(prev_rssi)
            # rssi increase, dog moves closer so bot keeps waiting
            if rssi > prev_rssi:
                state = "wait"
            # rssi decrease, dog moves further so go to search
            else:
                state = "search"

        elif state == "search":
            # robot run circle and find the right point
            rssi_max = circle(is_found)
            if is_found:
                print "find dog in search!"
                break
            # once find the max rssi point, turn 90 degrees to face to the right direction
            else:
                print "Turn 90 degrees to face your pet ;>"
                turn(1)
                state = "run"

        elif state == "run":
            is_found = forward(8, rssi_max)
            if is_found:
                print "find dog in run!"
                break

            else:
                state = "wait"
     

