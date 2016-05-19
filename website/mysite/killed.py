import time
import os
import subprocess

SLEEP_TIME = 15

p = subprocess.call("sudo hcidump -a > foo.txt &", shell = True)
time.sleep(SLEEP_TIME)
print "sleep over"
os.system("sudo kill " + str(p))

