import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a loop to plot and display data
for i in range(5):  # Repeat 5 times
    plt.plot(x, y1, label='Sin(x)')  # Plot the initial data
    plt.show()  # Display the plot
    plt.plot(x, y2, label='Cos(x)')  # Plot additional data over the existing plot
    plt.show()  # Display the updated plot

