import sys
from function import calc 
import sympy
from math import atan, degrees, acos, sqrt, asin

# Check if command-line arguments are provided, otherwise prompt user for input
if len(sys.argv) != 1:
    given = sys.argv  # Command-line arguments
else:
    given = input("Write as [V0] [Range] [Y0 (default is 0)]: ")  # User input if no arguments provided
    given = given.split(" ")
    given.insert(0, ".")

# Extract initial velocity and range from input
vI = float(given[1])
range = float(given[2])

# Convert the input ranges to floats
try:
    yI = float(given[3])
except:
    yI = 0

g = 10  # Gravitational acceleration constant

# Calculate launch angle based on whether there is an initial height or not
if yI != 0:
    h = yI
    theta = atan(range / h)  # Angle to reach the target range without initial height
    try:
        alpha = ((acos((((g * range ** 2) / vI ** 2) - h) / sqrt(h ** 2 + range ** 2))) - theta) / 2
        print(abs(degrees(alpha)))  # Print the launch angle in degrees
    except:
        print("Error, it won't reach the wanted range.")
else:
    try:
        alpha = (asin((g * range) / (vI ** 2)) / 2)  # Angle calculation when no initial height is provided
        print(degrees(alpha))  # Print the launch angle in degrees
    except:
        print("Error, it won't reach the wanted range.")
