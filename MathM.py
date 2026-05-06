# importing an entire module
import math
print(math.sqrt(25))
print(math.pi)
print(math.gcd(8,2))

# import a module using an alias
import math as m
print(m.log(10))
print(m.log2(8))

# import specific functions or variables
from math import perm,lcm
print(perm(5,2))
print(lcm(7))

# import all functions and variables
from math import*
print(sin(0))
print(cos(0))
print(tan(0))