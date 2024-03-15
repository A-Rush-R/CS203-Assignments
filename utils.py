from math import sqrt

def distance (pt1,pt2) :
    
    x1,y1 = pt1
    x2,y2 = pt2

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)