import numpy as np
import pandas as pd


class mainDialog(object):
    def __init__(self):

        #self.list = list
        self.dis = []
        #nameAndSignal = self.splitsplit(list)
        #self.name.set(nameAndSignal)


    def locate(self):

        signal = self.readCsv()
        #print(signal)
        #print(len(signal))

        for i in range(0, len(signal)):
            disTemp = self.signalToDis(signal[i])
            self.dis.append(disTemp)

        #print(self.dis)
        print(self.dis)


    def signalToDis(self, sig):
        A = 46
        n = 4.0
        return 10 ** ((-int(sig) - A) / (10 * n))



    def readCsv(self):
        data = pd.read_csv(r'C:\Users\asus\Desktop\6221Project\data\test001')
        list = data.values.tolist()
        aList = np.array(list)
        sigList = [x[4] for x in aList]
        #print(sigList)
        return sigList


d = mainDialog()
d.locate()

