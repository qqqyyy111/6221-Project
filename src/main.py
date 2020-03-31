import numpy as np
import pandas as pd

import algorithm
from wifiScan import scanWifi
import math



def get_namedist():
    #signal = self.readCsv()
    name = get_name()
    signal = get_signal()

    distance = []
    for i in range(0, len(signal)):
        disTemp = signalToDis(signal[i])
        distance.append(disTemp)

    namedist = []
    for i in range(len(name)):
        namedist.append([name[i], distance[i]])
    return namedist

    # location
    '''
    xc, yc = algorithm.intersection(self.points, self.radius)
    if xc == -1 and yc == -1:
        print('error')
    else:
        x1, y1 = (xc - 3), (yc - 3)
        x2, y2 = (xc + 3), (yc + 3)
      

    print(xc,yc)
    '''

def signalToDis(sig):
    A = 36
    n = 2.5
    return 10 ** ((-int(sig) - A) / (10 * n))

    #exp = (27.55-(20* math.log10(int(fre)/1000)) + abs(int(sig))) / 20.0
    #return math.pow(10.0, exp)

def readCsv():
    data = pd.read_csv(r'C:\Users\asus\Desktop\6221Project\data\test003')
    list = data.values.tolist()
    aList = np.array(list)
    sigList = [x[4] for x in aList]
    # print(sigList)
    return sigList

def get_signal():
    data = scanWifi()
    signal = []
    for i in range(0, len(data)):
        signal_temp = data[i][4]
        signal.append(signal_temp)
    #print(signal)
    return signal

def get_name():
    data = scanWifi()
    name = []
    for i in range(0, len(data)):
        name_temp = data[i][0]
        name.append(name_temp)
    return name

def get_freq():
    data = scanWifi()
    signal = []
    for i in range(0, len(data)):
        if data[i][0] == 'FiOS-S1MDM':
            freq_temp = data[i][5]
            print(freq_temp)
            return freq_temp
