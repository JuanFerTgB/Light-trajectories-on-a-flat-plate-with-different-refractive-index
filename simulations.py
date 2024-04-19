import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to calculate n(x, y)
def n(x, y):
    return np.sqrt(1 + y**2)

# Initial values for the exponential curves
x = np.linspace(-2, 2, 200)
y1 = np.exp(-x)
y2 = -np.exp(-x)
y3 = np.exp(x)
y4 = -np.exp(x)

# Plotting the exponential curves
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$y = e^{-x}$')
plt.plot(x, y2, label=r'$y = -e^{-x}$')
plt.plot(x, y3, label=r'$y = e^{x}$')
plt.plot(x, y4, label=r'$y = -e^{x}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Light Trajectories on a Flat Plate')
plt.legend()
plt.grid(True)
plt.show()

# Function to calculate the refractive index n(x, y)
def refractive_index(x, y):
    return np.sqrt(1 + y**2)

# Generating a grid of points in the (x, y) plane
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculating the refractive index at each point on the grid
n_vals = refractive_index(X, Y)

# Plotting the refractive index distribution
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, n_vals, cmap='viridis')
plt.colorbar(label='Refractive Index')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Refractive Index Distribution')
plt.grid(True)
plt.show()

# Defining the limits of the square
x_square = [0, 3, 3, 0, 0]
y_square = [0, 0, 1.5, 1.5, 0]

# Defining the limits of the semicircle
B = 3
A3 = 1.75
B2 = 1
A2 = 1
B3 = 2
A1 = 1.41
theta = np.linspace(np.pi, 0, 1000)
x_circle1 = np.sqrt(B) * np.cos(theta) + A3
x_circle2 = np.sqrt(B2) * np.cos(theta) + A2
x_circle3 = np.sqrt(B3) * np.cos(theta) + A1
y_circle = np.sqrt(B) * np.sin(theta)

# Defining the limits of the secondary trajectories
y_circle2 = np.sqrt(B2) * np.sin(theta)
y_circle3 = np.sqrt(B3) * np.sin(theta)

# Creating the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Adding the square to the plot
ax.add_patch(Rectangle((0, 0), 3.5, 3.5, linewidth=2, edgecolor='black', facecolor='none'))

# Plotting the square and the semicircle
ax.plot(x_circle2, y_circle2, 'b-', label='Trajectory with 1/y')
ax.plot(x_circle3, y_circle3, 'g-', label='Trajectory with 2/y')
ax.plot(x_circle1, y_circle, 'r-', label='Trajectory with 3/y')

# Adjusting the aspect ratio and showing the legend
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Light Trajectory on an Inhomogeneous Plate')
plt.grid(True)
plt.show()
