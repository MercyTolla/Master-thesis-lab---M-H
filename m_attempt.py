import numpy as np
import plotly.graph_objects as go
import math

a = (15/2) /100 # Half width of the pipe in m
b = (3/2) /100  # Half depth of the pipe in m
x = a           # Horizontal position (constant value for x)

# Function F(R)
def F(j, a, b):
    R = a / b
    lambda_j = (2 * j - 1) * math.pi / 2
    F = 1 - (192 / (R * math.pi**5)) * sum([math.tanh(lambda_j * R) / (2 * j - 1)**5 for j in range(1, 5)])
    return (F)

# Function to calculate T given U_avg
def T(j, b):
    a = (15/2) /100
    U_avg=0.2
    T = (3 * U_avg) / (2 * b**2 * F(j, a, b))
    return (T) #m/s

# # Function for the velocity field u(x, y) - USING CORNISH
def u_C(x, y, b, T, terms=5):
    result = - (32 * T * b**2) / np.pi**3 * (
        np.sum([(np.cosh(n * np.pi * x / (2 * b)) / np.cosh(n * np.pi * a / (2 * b))) * np.cos(n * np.pi * y / (2 * b)) 
                for n in range(0, terms + 1)])
    ) + T * (b**2 - y**2)

    return (result)
'''
# Function for the velocity field u(x, y) - USING HANKS
def u_H(x, y, T):
    lambda_j = lambda j: (2 * j - 1) * math.pi / 2
    A_j = lambda j: ((-1)**(j + 1)) / (2 * j - 1)**3
    eta = y / b
    xi = x / a
    result = T * b**2 * (1 - eta**2 - 32 / np.pi**3 * (np.sum([A_j(j) * np.cosh(lambda_j(j) * R * xi) / np.cosh(lambda_j(j) * R) * np.cos(lambda_j(j) * eta)
                  for j in range(1, 5)])))
    return (result)
'''

y_range = np.linspace(-b, b, 100) #unit m
from scipy.optimize import fsolve
# Solve for each value in the range
for y in y_range:
    # Use fsolve to find the root of the equation T(j) = 0
    T_y = lambda j: T(j, b=y)
    solution = fsolve(T_y, x0=1)  # Replace initial_guess with your initial guess for the root
    #solutions.append(solution[0]) 
    #velocity_values = [u_H(x, y_val, solution[0]) for y_val in y_range]
    velocity_values = [u_C(x, y_val, b, solution[0], terms=2) for y_val in y_range]

# Create a scatter plot using Plotly
fig = go.Figure(data=go.Scatter(x=y_range, y=velocity_values, mode='lines'))
fig.update_layout(
    xaxis_title='Vertical position [m]',
    yaxis_title='Velocity [m/s]',
    title='Velocity as a Function of Vertical Position'
)
fig.show()