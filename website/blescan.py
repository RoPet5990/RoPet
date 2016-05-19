import os
os.system("sudo hcidump -a | awk '/E3:/,/RSSI/' | awk '/RSSI/'")
