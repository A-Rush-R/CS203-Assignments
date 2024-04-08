import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the interval [A, B]
A = 10
B = 50

# define mean and standard deviation
# assuming that [A , B] is the range [mean - std, mean + std]
MEAN = (A + B) / 2
STD =  (B - A) / 2

# define bins for plotting the histogram
BINS = 100

# Sample numbers from A uniform distribution
N = 10000
random_numbers = np.random.rand(N)

# Calculate the inverse of the cumulative distribution function (CDF) of the Gaussian Distribution for each number
gaussian_random_numbers = []
for i in range(N):
    # percent point function, given a CDF value, returns the value of the RV (from normal distribution) at which would lead to this CDF
    gaussian_random_numbers.append(norm.ppf(random_numbers[i], loc= MEAN, scale = STD ))

# Plot A histogram using the random numbers generated in step 2
print ("Mean of sampled distribution is" , np.mean(gaussian_random_numbers))
print ("Variance of sampled distribution is", np.std(gaussian_random_numbers))
plt.hist(gaussian_random_numbers, bins = BINS)
plt.title('Gaussian Distribution within the interval [{}, {}]'.format(A, B))
plt.xlabel('Random Number')
plt.ylabel('Frequency')
plt.savefig("plot.png")
plt.show()