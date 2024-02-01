import numpy as np
import matplotlib.pyplot as plt
import Cornish as C

a = 3
b = 15
y = -b
T = C.T(C.U_avg)
mu = 3.6/1000 #cp

def shear_stress(x, y, a, b, T, y_wall, terms=5):
    gamma_w_y = - (32 * T * b**2) / np.pi**3 * (
        np.pi / (2 * b) * np.cosh(np.pi * x / (2 * b)) / np.cosh(np.pi * a / (2 * b)) * np.sin(np.pi * y_wall / (2 * b)) -
        (1 / 3**3) * (3 * np.pi / (2 * b)) * np.cosh(3 * np.pi * x / (2 * b)) / np.cosh(3 * np.pi * a / (2 * b)) * np.sin(3 * np.pi * y_wall / (2 * b))
    ) - 2 * T * y_wall
    res = gamma_w_y*mu

    return res



# Calculate shear stress at the bottom wall (y = -b)
shear_stress_values_minus_b = [shear_stress(x, y, a, b, T, -b, terms=5) for x in np.linspace(0, a, 100)]

plt.plot(np.linspace(-a, a, 100), shear_stress_values_minus_b, label='y = -b')
plt.xlabel('Horizontal position, [m]')
plt.ylabel('Shear Stress [Pa]')
plt.title('Shear Stress at the Wall')
plt.legend()
plt.show()