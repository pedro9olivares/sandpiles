import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

# Define the 5 points (x1, y1), ..., (x5, y5)
points = np.array([[0, 127], [42, 113], [85, 85], [113, 42], [127, 0]])  # Example points (5)

# Construct the matrix for the conic equation
A_matrix = []
b = []

for x, y in points:
    A_matrix.append([x**2, x*y, y**2, x, y, 1])
    b.append(0)

A_matrix = np.array(A_matrix)
b = np.array(b)

# Solve the homogeneous system using SVD (since it's underdetermined)
_, _, Vt = np.linalg.svd(A_matrix)
conic_coefficients = Vt[-1]  # Solution corresponding to the smallest singular value

# Extract coefficients
A, B, C, D, E, F = conic_coefficients

# Function to evaluate the conic
def conic(x, y):
    return A*x**2 + B*x*y + C*y**2 + D*x + E*y + F

# Load and display the matrix.npy file
matrix = np.load("state1_256x256.npy")

cmap = matplotlib.cm.Blues(np.linspace(0,1,20))
plt.imshow(matrix, cmap=matplotlib.colors.ListedColormap(cmap[10:,:-1]), extent=[0, matrix.shape[1], 0, matrix.shape[0]])
plt.colorbar()

# Generate grid for plotting the conic
x_vals = np.linspace(0, matrix.shape[1], 500)
y_vals = np.linspace(0, matrix.shape[0], 500)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)

# Evaluate the conic
conic_values = conic(x_grid, y_grid)

# Plot the conic contour
plt.contour(x_grid, y_grid, conic_values, levels=[0], colors='red')

# Plot the original points
for x, y in points:
    plt.scatter(x, y, color='g', s=9, zorder=5)

# Add the equation as a label
equation = f"{A}x² + {B}xy + {C}y² + {D}x + {E}y + {F} = 0"
print("The equation is:")
print(equation)
#plt.text(0.5, 5.5, equation, fontsize=10, color="black", bbox=dict(facecolor="white", alpha=0.5))
#plt.legend()

plt.title("Encontrando cónicas")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
