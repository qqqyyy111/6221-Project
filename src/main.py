import pywifi
import sys
import time
import os


from pywifi import const
from src.scanner import Scanner

scanner = Scanner()
def getAps():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # time.sleep(3)
    scanner.scan_all()

'''    iface.scan()
    data = iface.scan_results()
    for item in data:
        print(item.ssid)'''

getAps()
