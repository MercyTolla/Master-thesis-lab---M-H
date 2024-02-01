import numpy as np
import matplotlib.pyplot as plt
import Cornish as C

a = 3
b = 15
T = C.T(C.U_avg)
mu = 3.6/1000 #cp

def shear_stress(x, y, a, b, T, terms=5):
    sum_term = np.sum([
        (np.pi / (2 * b) * np.cosh(np.pi * x / (2 * b)) / np.cosh(np.pi * a / (2 * b)) * np.sin(np.pi * y / (2 * b))) -
        (1 / 3**3) * (3 * np.pi / (2 * b) * np.cosh(3 * np.pi * x / (2 * b)) / np.cosh(3 * np.pi * a / (2 * b)) * np.sin(3 * np.pi * y / (2 * b)))
        for n in range(1, terms + 1)
    ])
    
    gamma_w_y = - (32 * T * b**2) / np.pi**3 * sum_term - 2 * T * y
    
    res = abs(gamma_w_y)*mu

    return res

x_range = np.linspace(-a, a, 10)

# Calculate shear stress at the bottom wall (y = -b)
shear_stress_values_minus_b = [shear_stress(x, -b, a, b, T, terms=5) for x in x_range]

plt.plot(x_range, shear_stress_values_minus_b, label='y = -b')
plt.xlabel('Horizontal position, [m]')
plt.ylabel('Shear Stress [Pa]')
plt.title('Shear Stress at the Wall')
plt.legend()
plt.show()
#shear_stress(0, y, a, b, T, -b, terms=6)
#print(T)