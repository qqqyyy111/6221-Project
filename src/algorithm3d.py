import sys
import numpy as np

def trilaterate3D(data):
    # x,y,z
    p1 = np.array(data[0][:3])
    p2 = np.array(data[1][:3])
    p3 = np.array(data[2][:3])
    p4 = np.array(data[3][:3])
    # d radui
    r1 = data[0][-1]
    r2 = data[1][-1]
    r3 = data[2][-1]
    r4 = data[3][-1]

    e_x = (p2 - p1) / np.linalg.norm(p2 - p1)
    i = np.dot(e_x, (p3 - p1))

    e_y = (p3 - p1 - (i * e_x)) / (np.linalg.norm(p3 - p1 - (i * e_x)))
    e_z = np.cross(e_x, e_y)

    d = np.linalg.norm(p2 - p1)
    j = np.dot(e_y, (p3 - p1))

    x = ((r1 ** 2) - (r2 ** 2) + (d ** 2)) / (2 * d)
    y = (((r1 ** 2) - (r3 ** 2) + (i ** 2) + (j ** 2)) / (2 * j)) - ((i / j) * (x))

    #print(x)
    #print(y)
    z1 = np.sqrt(abs(r1 ** 2 - x ** 2 - y ** 2))
    z2 = np.sqrt(abs(r1 ** 2 - x ** 2 - y ** 2)) * (-1)

    ans1 = p1 + (x * e_x) + (y * e_y) + (z1 * e_z)
    ans2 = p1 + (x * e_x) + (y * e_y) + (z2 * e_z)
    dist1 = np.linalg.norm(p4 - ans1)
    dist2 = np.linalg.norm(p4 - ans2)
    if np.abs(r4 - dist1) < np.abs(r4 - dist2):
        return ans1
    else:
        return ans2

