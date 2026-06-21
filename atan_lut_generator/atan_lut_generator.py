import math
from fxpmath import Fxp

# Specify number of integer bits here
INTEGER_BITS = 4

# Specify number of fractional bits here
FRACTIONAL_BITS = 16

#-------------------------------------------

ATAN_LUT = []
for i in range(FRACTIONAL_BITS):
    ATAN_LUT.append(Fxp(math.atan(2**(-i)), dtype=f'U{INTEGER_BITS}.{FRACTIONAL_BITS}'))

PI = Fxp(math.pi, dtype=f'U{INTEGER_BITS}.{FRACTIONAL_BITS}')
print(f'Q{INTEGER_BITS}.{FRACTIONAL_BITS} of pi in hex is: {PI.hex()[2:]}')

# Write atan values to files

with open("./../rtl/atan_lut.mem", "w") as f:
    for i in range(FRACTIONAL_BITS):
        print(ATAN_LUT[i].hex()[2:], file=f)

with open("./../tb/sim_build/atan_lut.mem", "w") as f:
    for i in range(FRACTIONAL_BITS):
        print(ATAN_LUT[i].hex()[2:], file=f)

# Write PI to files

with open("./../rtl/pi.mem", "w") as f:
    print(PI.hex()[2:], file=f)

with open("./../tb/sim_build/pi.mem", "w") as f:
    print(PI.hex()[2:], file=f)
