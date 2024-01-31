import numpy as np
import matplotlib.pyplot as plt

tau = -1  # Example value???
a = 3       # Horizontal boundary condition 
b = 15      # Vertical boundary condition 
x = a       # Constant value for x
#mu = [0,1,2,3,4,5,6] #Viscosity 

# Plot of velocity as a function of vertical position in a rectangular channel 
def u(x, y, a, b, tau, terms=5):
    result = - (32 * tau * b**2) / np.pi**3 * (
        np.sum([(np.cosh(n * np.pi * x / (2 * b)) / np.cosh(n * np.pi * a / (2 * b))) * np.cos(n * np.pi * y / (2 * b)) 
                for n in range(1, terms + 1)])
    ) + tau * (b**2 - y**2)

    return result

# Define the range for y (vertical position)
y_range = np.linspace(0, b, 100)

# Use the constant value of x for all points in the range
x_values = np.full_like(y_range, fill_value=x)

# Compute the velocity field for each point in the range of y
velocity_values = u(x_values, y_range, a, b, tau, terms=5)

# Plot the velocity field
plt.plot(y_range, velocity_values)
plt.xlabel('Vertical Position, y [cm]')
plt.ylabel('Velocity [cm/s]')
plt.title('Velocity as a Function of Vertical Position')
plt.show()