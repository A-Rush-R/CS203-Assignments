import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def prob_ratio(n, k):
    if n <= k + 1:
        return np.nan
    doors = ['C' for _ in range(k)]
    doors += ['G' for _ in range(n-k)]
    num = 5000

    win_og = 0
    win_sw = 0
    for i in range(num):
        choice = np.random.randint(0, n)
        if doors[choice] == 'C':
            win_og += 1
        if choice == n - 1:
            choice = n - 2
        new_choice = np.random.randint(0, n - 1)
        while new_choice == choice:
            new_choice = np.random.randint(0, n - 1)
        if doors[new_choice] == 'C':
            win_sw += 1
        
    prob_og = float(win_og) / num
    prob_sw = float(win_sw) / num

    return prob_sw / prob_og

def prob_ratio_exact(n, k):
    if n <= k + 1:
        return np.nan
    else:
        return (n - 1)/(n - 2)

# Make data for the first surface.
N = 100
n = np.arange(3, N, 1)
k = np.arange(1, N - 2, 1)
n, k = np.meshgrid(n, k)
vectorized_prob_ratio = np.vectorize(prob_ratio)
vectorized_prob_ratio_exact = np.vectorize(prob_ratio_exact)
Z = vectorized_prob_ratio(n, k)

# Plot the first surface.
surf = ax.plot_surface(n, k, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Make data for the second surface (initially set to a plane).
Z_exact = vectorized_prob_ratio_exact(n, k)

# Plot the second surface (plane).
surf_plane = ax.plot_surface(n, k, Z_exact, color='yellow', alpha=0.5)

# Customize the z axis.
ax.set_zlim(0.5, 2.5)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()