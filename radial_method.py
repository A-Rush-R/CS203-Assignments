import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math


def radial_method ():
    rng = np.random.default_rng()

    # Let radius be 1 unit.

    radius = 1

    # The Random Radial Point Method
    # 
    # In this approach we draw a chord perpendicular to endpoint of some radius less than or equal to $r$. We sample radius from uniform distribution over [0,radius]. 
    # 
    # Any radius less than $radius/2$ has a corresponding chord that is greater than the side.

    l = 1000
    Sample = []
    for i in range(l):
        Sample.append(rng.uniform(0, radius))


    distribution = []
    for i in range(l):
        distribution.append(Sample[i] < radius/2)


    avg = [sum(distribution[:i])/i for i in range(1,l+1)]

    plt.title("The Random Radial Point Method")
    plt.xlabel("Number of Trials")
    plt.ylabel("Proportion of Chords Longer than the side")
    plt.axis([0,l,0,1])

    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,0.25,0.5,0.75,1])
    plt.plot(range(1,l+1), avg)
    plt.show()