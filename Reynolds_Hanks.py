import math 

# Given variables
x = 1 #?
y = 1 #?
a = 3
b = 15
R = a / b

# Check for symmetric case
if R == 1:
    xi = 0
else: 
    xi = x / a
    
eta = y / b

def F(R):
    lambda_j = lambda j: (2 * j - 1) * math.pi / 2
    F = 1 - (192 / (R * math.pi**5)) * sum(math.tanh(lambda_j(j) * R) / (2 * j - 1)**5 for j in range(1, 101))
    return F


def u(R):
    m = 1.7 + 0.5 * R**1.4
    #Calculate n based on the value of R
    if R > 3:
        n = 2
    elif R < 3:
        n = 2 + 0.3 * ((1 / R) - (1 / 3)) 
    u = ((m + 1) / m) * ((n + 1) / n) * (1 - xi**m) * (1 - eta**n)
    partial_u_xi = (eta**n - 1) * (m + 1) * (n + 1) * xi**(m - 1) / n
    partial_u_eta = (m + 1) * (n + 1) * (xi**m) * eta**(n - 1) / m
    Z = u * math.sqrt((1 / R**2) * (partial_u_xi**2) + (partial_u_eta**2))
    return Z

def Reynolds_H(R):
    Z = u(R)
    F_ = F(R)
    Re_c = (4848*R)/((1+R)*F_*Z)
    return Re_c

print(u(1))
print(F(1))
print("Reynolds number: ", round(Reynolds_H(1), 2))


    
        