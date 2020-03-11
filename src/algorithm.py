import math

def intersection(points, radius):
    linePoints = []
    for i in range(3):
        # Center distance
        AB = twoPointDis(points[i]['x'], points[i]['y'], points[(i + 1) % 3]['x'], points[(i + 1) % 3]['y'])
        # If the 3 circles do not intersect each other, an error is reported
        if AB >= radius[i] + radius[(i + 1) % 3] or AB <= abs(radius[i] - radius[(i + 1) % 3]):
            return -1, -1

        # 3 circles intersect in pairs, find their common areas
        else:
            k = slopeRecip(points[i]['x'], points[i]['y'], points[(i + 1) % 3]['x'], points[(i + 1) % 3]['y'])
            theta = math.atan(k)  # Angle between cosecant CD and X axis
            AE = (pow(AB, 2) - pow(radius[(i + 1) % 3], 2) + pow(radius[i], 2)) / (2 * AB)
            CE = math.sqrt(pow(radius[i], 2) - pow(AE, 2))
            CE = math.sqrt(pow(radius[(i + 1) % 3], 2) - pow(AB-AE, 2))
            # Midpoint coordinates
            xe = points[i]['x'] + (points[(i + 1) % 3]['x'] - points[i]['x']) * AE / AB
            ye = points[i]['y'] + (points[(i + 1) % 3]['y'] - points[i]['y']) * AE / AB

            # Secant endpoint coordinates
            linePoints.append({'x': xe + CE * math.cos(theta), 'y': ye + CE * math.sin(theta)})
            linePoints.append({'x': xe - CE * math.cos(theta), 'y': ye - CE * math.sin(theta)})


    return lineIntersection(linePoints)


def twoPointDis(x1, y1, x2, y2):
    return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


# Find the slope of the common secant of two circles
def slopeRecip(x1, y1, x2, y2):
    if y2 != y1:
        k = -(x2 - x1) / (y2 - y1)
    else:
        k = float('-inf')
    return k


# Find line intersection
def lineIntersection(linePoints):
    x1 = linePoints[0]['x']
    y1 = linePoints[0]['y']
    x2 = linePoints[1]['x']
    y2 = linePoints[1]['y']

    x3 = linePoints[2]['x']
    y3 = linePoints[2]['y']
    x4 = linePoints[3]['x']
    y4 = linePoints[3]['y']

    if x1 == x2:
        xs = x1
        k = (y4 - y3) / (x4 - x3)
        b = y3 - k * x3
        ys = k * xs + b
        return xs, ys
    elif x3 == x4:
        xs = x3
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        ys = k * xs + b
        return xs, ys
    else:
        k1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - k1 * x1
        k2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - k2 * x3
        xs = (b2 - b1) / (k1 - k2)
        ys = k1 * xs + b1
        return xs, ys