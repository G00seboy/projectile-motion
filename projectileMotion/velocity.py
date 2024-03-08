import sys
from function import calc  
from math import asin, degrees, sqrt, sin, radians

# Check if command-line arguments are provided
if len(sys.argv) != 1:
    given = sys.argv
else:
    # If no command-line arguments, prompt user for input
    given = input("Write as [Range] [angle] [Y0 (default is 0)]: ")
    given = given.split(" ")
    given.insert(0, ".")  # Insert a dummy argument to match indexing with command-line input

range = float(given[1])  # Extract the target range from input

try:
    angle = float(given[2])  # Extract the angle from input if provided
except:
    angle = 45  # Default angle is set to 45 degrees

# Calculate initial velocity using the provided range and angle
vI = sqrt((range * 10) / (sin(radians(2 * angle))))

print(f"Use rocket of {vI} m/s")  # Output the calculated initial velocity
