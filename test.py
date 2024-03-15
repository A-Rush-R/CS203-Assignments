import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')

# Set x and y limits
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])

# Plot the unit circle
circle = plt.Circle((0, 0), 1, color='b', fill=False)
ax.add_artist(circle)

# Initialize an empty list to store points
points = []

# Plot the initial point
point, = ax.plot([], [], 'ro',markersize=1)

# Update function to plot a random point in the unit circle and retain previous points
def update(frame):
    # Generate random coordinates within the unit circle
    x, y = np.random.uniform(-1, 1, 2)
    while x**2 + y**2 > 1:  # Ensure the point is inside the unit circle
        x, y = np.random.uniform(-1, 1, 2)
    points.append((x, y))  # Store the new point
    # Plot all points
    point.set_data(*zip(*points))
    return point,

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=100, blit=True, interval=1)

plt.show()
