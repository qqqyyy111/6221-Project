import numpy as np
import pandas as pd

import algorithm
import wifiScan
import math


class mainLocate():
    def __init__(self):
        self.points = [
            {'x':330,'y':234},
            {'x':221,'y':96},
            {'x':197,'y':179}
        ]

        self.radius = [119.7,126.8,150]
        self.dis = []
        self.precision = 0.25

    def locate(self):
        signal = self.readCsv()
        for i in range(0, len(signal)):
            disTemp = self.signalToDis(signal[i])
            self.dis.append(disTemp)
            #self.radius.append(disTemp / self.precision * 20)


        # location
        xc, yc = algorithm.intersection(self.points, self.radius)
        '''if xc == -1 and yc == -1:
            print('error')
        else:
            x1, y1 = (xc - 3), (yc - 3)
            x2, y2 = (xc + 3), (yc + 3)'''

        print(xc,yc)



    def signalToDis(self, sig):
        A = 46
        n = 4.0
        return 10 ** ((-int(sig) - A) / (10 * n))

    def readCsv(self):
        data = pd.read_csv(r'C:\Users\asus\Desktop\6221Project\data\test003')
        list = data.values.tolist()
        aList = np.array(list)
        sigList = [x[4] for x in aList]
        # print(sigList)
        return sigList


if __name__ == '__main__':
    l = mainLocate()
    l.locate()
