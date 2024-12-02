import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define three points in the positive quadrant
points = np.array([[0, 130], [84, 84], [126, 0]])  # Example points (3)
#points = np.array([[0, 130], [84, 84], [126, 0], [41, 116]])  # Example points (4)
#points = np.array([[0, 130], [84, 84], [126, 0], [41, 116], [112, 40]])  # Example points (5)
x_points, y_points = points[:, 0], points[:, 1]

# Step 2: Fit a quadratic curve (y = ax^2 + bx + c)
coefficients = np.polyfit(x_points, y_points, 2)  # Degree 2 for quadratic
a, b, c = coefficients

# Define a function for the quadratic curve
def quadratic_curve(x):
    return a * x**2 + b * x + c

print(f'The coefficients are a = {a}, b = {b}, c = {c}')

# Generate x values for plotting the curve
x_curve = np.linspace(min(x_points), max(x_points), 500)
y_curve = quadratic_curve(x_curve)

# Step 3: Load the matrix and graph it
matrix = np.load('state1_256x256.npy')

plt.figure(figsize=(10, 6))

# Plot the matrix as an image
plt.imshow(matrix, cmap='viridis', extent=[0, matrix.shape[1], 0, matrix.shape[0]], origin='lower')

# Superimpose the quadratic curve
plt.plot(x_curve, y_curve, color='red', label=f'y = {a:.2f}x² + {b:.2f}x + {c:.2f}')

# Scatter plot the original points
plt.scatter(x_points, y_points, s=5, color='white', label='Original Points')

# Add labels and legend
plt.title('Quadratic Curve Fit')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()
