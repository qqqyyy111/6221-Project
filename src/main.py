import numpy as np
import pandas as pd

import algorithm
from wifiScan import scanWifi
import math


class mainLocate():
    def __init__(self):
        self.points = [
            {'x': 0.1, 'y': 5.3},
            {'x': 0.1, 'y': 0.1},
            {'x': 3.8, 'y': 0.1}
        ]

        self.radius = [6.094, 2.758, 2.191]
        self.dis = []
        #self.precision = 0.25

    def locate(self):
        #signal = self.readCsv()
        freq = self.get_freq()
        signal = self.get_signal()
        distance = self.signalToDis(freq, signal)
        print(distance)
        '''
        for i in range(0, len(signal)):
            disTemp = self.signalToDis(signal[i])
            self.dis.append(disTemp)
        '''
            #self.radius.append(disTemp / self.precision * 20)

        # location
        xc, yc = algorithm.intersection(self.points, self.radius)

        '''if xc == -1 and yc == -1:
            print('error')
        else:
            x1, y1 = (xc - 3), (yc - 3)
            x2, y2 = (xc + 3), (yc + 3)
        '''

        print(xc,yc)


    def get_wifi(self):
        pass


    def signalToDis(self, fre, sig):
        # A = 38
        # n = 3.25
        # return 10 ** ((-int(sig) - A) / (10 * n))

        exp = (27.55-(20* math.log10(int(fre)/1000)) + abs(int(sig))) / 20.0
        return math.pow(10.0, exp)

    def readCsv(self):
        data = pd.read_csv(r'C:\Users\asus\Desktop\6221Project\data\test003')
        list = data.values.tolist()
        aList = np.array(list)
        sigList = [x[4] for x in aList]
        # print(sigList)
        return sigList

    def get_signal(self):
        data = scanWifi()
        signal = []
        for i in range(0, len(data)):
            if data[i][0] == 'FiOS-S1MDM':
                signal_temp = data[i][4]
                print(signal_temp)
                return signal_temp
                #signal.append(signal_temp)
        #print(signal_temp)
    def get_freq(self):
        data = scanWifi()
        signal = []
        for i in range(0, len(data)):
            if data[i][0] == 'FiOS-S1MDM':
                freq_temp = data[i][5]
                print(freq_temp)
                return freq_temp


if __name__ == '__main__':
    l = mainLocate()
    l.locate()
    #l.get_signal()