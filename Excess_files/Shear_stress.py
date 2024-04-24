import numpy as np
import matplotlib.pyplot as plt
import Excess_files.Cornish as C

a = 15/100 #m
b = 3/100 #m
T = C.T(C.U_avg)
mu = 3.6*0.001  #Centipoise (cp) to pascal-second (Pa·s) 
R = a/b

def shear_stress(x, y, T, terms=5):
    lambda_j = lambda j: (2 * j - 1) * np.pi / (2 * b)
    A_j = lambda j: ((-1)**(j + 1)) / ((2 * j - 1)**3)
    xi = x / a
    sum_term = np.sum([
        (A_j(n) * np.cosh(lambda_j(n) * R * xi) / np.cosh(lambda_j(n) * R) * np.sin(lambda_j(n)))
        for n in range(1, terms + 1)
    ])
    
    gamma_w_y = T * b * (2 - 32 / np.pi**3 * sum_term)
    
    res = abs(gamma_w_y) * mu

    return res

x_range = np.linspace(-a/100, a/100, 100) #unit m

# Calculate shear stress at the bottom wall (y = -b)
shear_stress_values_minus_b = [shear_stress(x, -b, T, terms=5) for x in x_range]

plt.plot(x_range, shear_stress_values_minus_b, label='y = -b')
plt.xlabel('Horizontal position, [m]')
plt.ylabel('Shear Stress [Pa]')
plt.title('Shear Stress at bottom wall')
plt.legend()
plt.show()
