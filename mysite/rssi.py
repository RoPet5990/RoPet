import time
import os
import subprocess
import psutil

SLEEP_TIME = 15
NAME="hcidump"

def rssimean():
    rssi_sum = 0
    rssi_max = 0
    rssi_min = 0
    value = []  # RSSI value list
    
    while(rssi_sum == 0 or len(value) < 10):
        # write hcidump into txt
        p = subprocess.Popen("sudo hcidump -a > foo.txt &", shell = True)
        time.sleep(SLEEP_TIME)
        #print "sleep over"
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
        if len(value) >= 10:
            # find rssi_max and rssi_min
            rssi_max = value[0]
            rssi_min = value[0]
            for v in value:
                if v >= rssi_max:
                    rssi_max = v
                if v <= rssi_min:
                    rssi_min = v
            print "rssi_max is %s" %(rssi_max)
            print "rssi_min is %s" %(rssi_min)
            value = [x for x in value if x != rssi_max]
            value = [x for x in value if x != rssi_min]
#            value.remove(rssi_max)
#            value.remove(rssi_min)
            
            for v in value:
                if v >= rssi_max:
                    rssi_max = v
                if v <= rssi_min:
                    rssi_min = v
            print "rssi_max is %s" %(rssi_max)
            print "rssi_min is %s" %(rssi_min)
            value = [x for x in value if x != rssi_max]
            value = [x for x in value if x != rssi_min]
            
            if len(value) >= 10:
                print "after value: ", value
                if rssi_sum != 0:
                    rssi_sum = 0
                for v in value:
                    rssi_sum += float(v) 
                if rssi_sum != 0:           
                    rssi_mean = rssi_sum * 1.0 / len(value)
                    #print "rssi_mean: %s" %(str(rssi_mean))
        
                
    text_file.close()
    print "rssi_mean is %s" %(rssi_mean)
    return rssi_mean

