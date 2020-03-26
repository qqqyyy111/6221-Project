import pywifi
import time
import pandas as pd
import re
import math
from sqlalchemy import create_engine


NONE = 0
CIPHER_TYPE_WEP = 1
CIPHER_TYPE_TKIP = 2
CIPHER_TYPE_CCMP = 3
CIPHER_TYPE_UNKNOWN = 4

AUTH_TYPES = ['OPEN', 'SHARED']
KEY_TYPES = ['NONE', 'WPA', 'WPAPSK', 'WPA2', 'WPA2PSK', 'UNKNOWN']
CIPHER_TYPES = ['NONE', 'WEP', 'TKIP', 'CCMP', 'UNKNOWN']
wifilist = []
sleepTime = 3


def textPos(string, width):
    if len(string) > width - 1:
        string = string[0:width - 1]
    return string.ljust(width) + '|'


def existMac(mac):
    for l in wifilist:
        if l[1] == mac:
            return True


def scanWifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(sleepTime)
    scanRes = iface.scan_results()

    for id, profile in enumerate(scanRes):
        if existMac(profile.bssid):
            continue

        wifi = []

        #get name
        name = profile.ssid
        wifi.append(name)

        #get mac address
        mac = profile.bssid
        #mac = re.sub(':', '', mac)
        #mac_int = int(mac, 16)
        wifi.append(mac)

        #get auth_types
        auth = AUTH_TYPES[profile.auth[0]]
        wifi.append(auth)

        #get key_types
        type = KEY_TYPES[profile.akm[0]]
        wifi.append(type)

        #get signal
        signal = str(profile.signal)
        wifi.append(signal)

        freq = str(profile.freq)
        wifi.append(freq)

        wifilist.append(wifi)
        #print(wifi)

    return wifilist

def write_to_csv():
    #list = self.wifilist
    df = pd.DataFrame(list, columns=["ssid", "bssid", "auth_types", "key_types", "signal", "freq"])
    df.to_csv(r"C:\Users\asus\Desktop\6221Project\data\test005", index=False)

def write_to_mysql():
    list = wifilist
    engine = create_engine('mysql+pymysql://root:971005@localhost:3306/wifi?charset=utf8')
    df = pd.DataFrame(list, columns=["ssid", "bssid", "auth_types", "key_types", "signal", "frequency"])
    df.to_sql(name='wifi_info', con=engine, if_exists='append', index=False)



scanWifi()
write_to_mysql()
