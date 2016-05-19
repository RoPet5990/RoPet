import time
import os
import subprocess
import psutil

SLEEP_TIME = 3
NAME="hcidump"

def rssimean():
    rssi_sum = 0
    value = []  # RSSI value list
    while(rssi_sum == 0 or len(value) < 11):
        # write hcidump into txt
        p = subprocess.Popen("sudo hcidump -a > foo.txt &", shell = True)
        time.sleep(SLEEP_TIME)
        print "sleep over"
        for proc in psutil.process_iter():
            if proc.name() == NAME:
                proc.kill()

        # get rssi of our ble
        text_file = open("foo.txt", "r")
        content = text_file.read()
        line = content.split("> HCI Event: LE Meta Event") # list of every event
        list = []  # list of events which contains Adafruit BLE
        for one in line:
            if "E3:49:48:1C:4D:E6" in one:
                list.append(one)
        for e in list:
            start = e.find("RSSI:")
            end = e.find("\n", start)
            r = e[(start + 6):(end)]
            value.append(r)

        # calculate rssi mean in this timestamp
        print "value is ", value
        for v in value:
            rssi_sum += float(v) 
        if rssi_sum != 0:           
            rssi_mean = rssi_sum * 1.0 / len(value)
            print "rssi_mean is %s" %(str(rssi_mean))

    text_file.close()        
    return rssi_mean

