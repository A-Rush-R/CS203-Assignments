import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math

def mid_point_method () :
    rng = np.random.default_rng()

    # Let radius be 1 unit.

    radius = 1

    
    # Random Mid-Point Method
    # 
    # Let us draw the chord in such a way that a random point is chosen inside the circle, then a chord is drawn perpendicular to the line joining center and the the point, passing through the point. Then any chord with mid point lying more than half the radius from center is greater than equilateral triangle.


    def generate_point():
        point = []
        x = rng.uniform(-radius, radius)
        y = rng.uniform(-radius, radius)
        while x**2 + y**2 > radius**2:
            x = rng.uniform(-radius, radius)
            y = rng.uniform(-radius, radius)
        point.append(x)
        point.append(y)
        return point


    n = 1000
    Sample = []
    for i in range(n):
        Sample.append(generate_point())


    distance = []
    for i in range(n):
        distance.append(math.sqrt(Sample[i][0]**2 + Sample[i][1]**2))


    distribution = []
    for i in range(n):
        distribution.append(distance[i] < 0.5)


    avg = [sum(distribution[:i])/i for i in range(1,n+1)]

    plt.title("The Random Mid-Point Method")
    plt.xlabel("Number of Trials")
    plt.ylabel("Proportion of Chords Longer than the side")
    plt.axis([0,n,0,1])

    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,0.25,0.5,0.75,1])
    plt.plot(range(1,n+1), avg)
    plt.show()