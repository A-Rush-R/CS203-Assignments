import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the interval [a, b]
a = 10
b = 50

# Generate random numbers from a uniform distribution within the interval [0,1]
n = 10000
random_numbers = np.random.rand(n)

# Calculate the inverse of the cumulative distribution function (CDF) of the Gaussian Distribution for each random number
gaussian_random_numbers = np.zeros(n)
for i in range(n):
    gaussian_random_numbers[i] = norm.ppf(random_numbers[i], loc=(a+b)/2, scale=(b-a)/6)

# Plot a histogram using the random numbers generated in step 2
plt.hist(gaussian_random_numbers, bins=100)
plt.title('Gaussian Distribution within the interval [{}, {}]'.format(a, b))
plt.xlabel('Random Number')
plt.ylabel('Frequency')
plt.show()