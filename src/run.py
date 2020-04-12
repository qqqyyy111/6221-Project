from algorithm3d import trilaterate3D
from wifiScan import scanWifi
from main import get_namedist
from database import *
from algorithm import intersection

import numpy as np

#dist1 = get_namedist()
#dist2 = get_namedist()
#dist3 = get_namedist()
#dist4 = get_namedist()

distant2 = 19.054607179632473
distant3 = 2.7542287033381663
distant4 = 7.5857757502918375


sql1 = "select * from wifi1_distance1;"
wifi1_distance1 = db_query_datas(sql1)

sql2 = "select * from wifi1_distance2;"
wifi1_distance2 = db_query_datas(sql2)

sql3 = "select * from wifi1_distance3;"
wifi1_distance3 = db_query_datas(sql3)

sql4 = "select * from wifi1_distance4;"
wifi1_distance4 = db_query_datas(sql4)

sql5 = "select * from wifi_locate2d;"
wifi_locate2d = db_query_datas(sql5)


# find 4 wifi coordinates
def wifi_locate():
        wifilocation = []
        for i in range(0, len(wifi1_distance1)):
                data = [[0, 0, 0, float(wifi1_distance1[i][1])],
                        [4, 9, 0, float(wifi1_distance2[i][1])],
                        [9.8, 6.6, 0, float(wifi1_distance3[i][1])],
                        [6, 4.8, 2, float(wifi1_distance4[i][1])]]

                location = trilaterate3D(data)
                location = location.tolist()
                wifilocation.append(location)
        return wifilocation


def find_locate3d():
        wifilocation = wifi_locate()
        x = get_namedist()
        #print(x)
        for i in range(0, len(x)):
                if x[i][0] == 'FiOS-S1MDM-5G':
                        distance1 = x[i][1]
                        #print(distance1)
                elif x[i][0] == 'Jhomny':
                        distance2 = x[i][1]
                        #print(distance2)
                elif x[i][0] == 'Skynet':
                        distance3 = x[i][1]
                        #print(distance3)
                elif x[i][0] == 'Fios-T2CGS':
                        distance4 = x[i][1]
                        #print(distance4)


        data = [[wifilocation[0][0], wifilocation[0][1], wifilocation[0][2], distance1],
                [wifilocation[1][0], wifilocation[1][1], wifilocation[1][2], distant2],
                [wifilocation[2][0], wifilocation[2][1], wifilocation[2][2], distant3],
                [wifilocation[3][0], wifilocation[3][1], wifilocation[3][2], distant4]]

        location = trilaterate3D(data)
        location_list = location.tolist()
        #print(location_list)
        return location_list



def find_locate2d():
        radius = []
        x = get_namedist()
        for i in range(0, len(x)):
                if x[i][0] == 'FiOS-S1MDM-5G':
                        distance1 = x[i][1]
                        #print(distance1)
                elif x[i][0] == 'Jhomny':
                        distance2 = x[i][1]
                        #print(distance2)
                elif x[i][0] == 'Skynet':
                        distance3 = x[i][1]
                        #print(distance3)

        radius = [distance1, 19.054607179632473, 2.7542287033381663 ]
        points = [
                {'x': wifi_locate2d[0][0] , 'y': wifi_locate2d[0][1]},
                {'x': wifi_locate2d[1][0] , 'y': wifi_locate2d[1][1]},
                {'x': wifi_locate2d[2][0] , 'y': wifi_locate2d[2][1]}
        ]

        xc, yc = intersection(wifi_locate2d, radius)
        print(xc,yc)

