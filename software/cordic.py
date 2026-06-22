import math
import matplotlib.pyplot as plt
import numpy as np
from fxpmath import Fxp

integer_bits = 4
fractional_bits = 16

desired_angle = Fxp(math.pi/2, dtype=f'S{integer_bits}.{fractional_bits}')

atan_table = []
for i in range(fractional_bits):
    atan_table.append(Fxp(math.atan(2**(-i)), dtype=f'S{integer_bits}.{fractional_bits}'))
    # print(atan_table[i])

O = [0]*fractional_bits
X = []
Y = []

factor = 1

if ((Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}') <= desired_angle <= Fxp(math.pi, dtype=f'S{integer_bits}.{fractional_bits}'))):
    x = Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}')
    y = Fxp(1, dtype=f'S{integer_bits}.{fractional_bits}')
    current_angle = Fxp(math.pi/2, dtype=f'S{integer_bits}.{fractional_bits}')
elif ((Fxp(math.pi, dtype=f'S{integer_bits}.{fractional_bits}') <= desired_angle <= Fxp(2*math.pi, dtype=f'S{integer_bits}.{fractional_bits}'))):
    x = Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}')
    y = Fxp(-1, dtype=f'S{integer_bits}.{fractional_bits}')
    current_angle = Fxp(3*math.pi/2, dtype=f'S{integer_bits}.{fractional_bits}')
elif ((Fxp(-math.pi, dtype=f'S{integer_bits}.{fractional_bits}') <= desired_angle <= Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}'))):
    x = Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}')
    y = Fxp(-1, dtype=f'S{integer_bits}.{fractional_bits}')
    current_angle = Fxp(-math.pi/2, dtype=f'S{integer_bits}.{fractional_bits}')
else:
    x = Fxp(0, dtype=f'S{integer_bits}.{fractional_bits}')
    y = Fxp(1, dtype=f'S{integer_bits}.{fractional_bits}')
    current_angle = Fxp(-3*math.pi/2, dtype=f'S{integer_bits}.{fractional_bits}')

for i in range(fractional_bits):
    X.append(x)
    Y.append(y)

    print(f'Desired angle = {desired_angle*180/(math.pi)}')
    print(f'Current angle = {current_angle*180/(math.pi)}')
    print(f'Difference in angles = {(desired_angle - current_angle)*180/(math.pi)}')
    # print()
    if (desired_angle - current_angle < 0):
        sign = -1
    else:
        sign = 1

    current_angle = current_angle + sign*atan_table[i]

    # Iterate a maximum of width(fractional_bits) else 2**(-i) goes to zero
    x_next = x - sign*(1/(2**i))*y
    y_next = sign*(1/(2**i))*x + y

    x = x_next
    y = y_next

    factor = factor*(1/((1 + 2**(-2*i))**(1/2)))

    print(f'x at i = {i + 1}: {x}')
    print(f'y at i = {i + 1}: {y}')
    print()

print(f'True value of cos(desired_angle): {math.cos(desired_angle)}')
print(f'True value of sin(desired_angle): {math.sin(desired_angle)}')
print(f'True value of cos(desired_angle)/factor: {math.cos(desired_angle)/factor}')
print(f'True value of sin(desired_angle)/factor: {math.sin(desired_angle)/factor}')
print(factor)

# theta = np.linspace(0, 2*np.pi, 150)
# radius = 1
# a = radius*np.cos(theta)
# b = radius*np.sin(theta)
# plt.plot(a, b, color='b')

# plt.quiver(O[0:fractional_bits - 1], O[0:fractional_bits - 1], X[0:fractional_bits - 1], Y[0:fractional_bits - 1], angles='xy', scale_units='xy', scale=1, width=0.005)
# plt.quiver(0, 0, math.cos(desired_angle), math.sin(desired_angle), angles='xy', scale_units='xy', scale=1, color='b', width=0.005)
# plt.xlim(-2, 2)
# plt.ylim(-2, 2)

# plt.gca().set_aspect('equal')
# plt.grid()
# plt.show()
