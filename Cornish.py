import numpy as np
import matplotlib.pyplot as plt
import math

a = 15       # Half width of the pipe in cm
b = 3        # Half depth of the pipe in cm
x = a        # Horizontal position (constant value for x)
R = a / b    # Aspect ratio

# Function F(R)
def F(R):
    lambda_j = lambda j: (2 * j - 1) * math.pi / 2
    F = 1 - (192 / (R * math.pi**5)) * sum(math.tanh(lambda_j(j) * R) / (2 * j - 1)**5 for j in range(1, 101))
    return F

# Function to calculate T given U_avg
def T(U_avg):
    T = (3 * U_avg) / (2 * b**2 * F(R))
    return T

# # Function for the velocity field u(x, y) - USING CORNISH
def u_C(x, y, a, b, T, terms=5):
    result = - (32 * T * b**2) / np.pi**3 * (
        np.sum([(np.cosh(n * np.pi * x / (2 * b)) / np.cosh(n * np.pi * a / (2 * b))) * np.cos(n * np.pi * y / (2 * b)) 
                for n in range(1, terms + 1)])
    ) + T * (b**2 - y**2)

    return abs(result)

# Function for the velocity field u(x, y) - USING HANKS
def u_H(x, y, a, b, T, terms=5):
    lambda_j = lambda j: (2 * j - 1) * math.pi / 2
    A_j = lambda j: ((-1)**(j + 1)) / (2 * j - 1)**3
    eta = y / b
    xi = x / a
    result = T * b**2 * (1 - eta**2 - 32 / np.pi**3 * (np.sum([A_j(j) * np.cosh(lambda_j(j) * R * xi) / np.cosh(lambda_j(j) * R) * np.cos(lambda_j(j) * eta)
                  for j in range(1, terms + 1)])))
    return abs(result)

# Define the range of y values
y_range = np.linspace(-b, b, 1000)
#x_range = np.linspace(-a, a, 20)

# Set the value for U_avg (this will determine the shear stress T)
U_avg = 0.2  # m/s

# Calculate T using the provided U_avg value
T_value = T(U_avg * 100)

# Compute the velocity field for each point in the range of y (note: x is constant)
velocity_values = [u_C(x, y_val, a, b, T_value, terms=10) for y_val in y_range]

# Plot the velocity field
plt.plot(y_range, velocity_values)
plt.xlabel('Vertical position, [cm]')
plt.ylabel('Velocity [cm/s]')
plt.title('Velocity as a Function of Vertical Position')
plt.show()



