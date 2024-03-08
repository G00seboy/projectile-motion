import sys
from math import sin, cos, radians
import math
from sympy import *
from sympy.solvers import solve

# Function to perform calculations
def calc(given):
    # Extract given values from the input list
    vI = float(given[1])  # Initial velocity
    b = radians(float(given[2]))  # Angle in radians

    try:
        yI = float(given[3])  # Initial height (if provided)
    except:
        yI = 0.0  # Default initial height to 0 if not provided

    # Define symbol for time
    t = Symbol("t")

    # Acceleration components (assuming constant acceleration)
    a = [0, -10]  # Acceleration in x and y directions respectively

    # Initial velocity components
    v = [
        integrate(a[0], t) + (vI * cos(b)),  # Initial velocity in x direction
        integrate(a[1], t) + (vI * sin(b))   # Initial velocity in y direction
    ]

    # Position components
    r = [
        integrate(v[0], t),                 # Position in x direction
        integrate(v[1], t) + yI            # Position in y direction (including initial height)
    ]

    # Time to reach maximum height (when vertical velocity component becomes 0)
    tM = solve(v[1], t)[0]

    # Maximum height
    yM = r[1].subs(t, tM).evalf()

    # Time to hit the ground (when y position becomes 0)
    try:
        tF = solve(r[1], t)[1]  # If there are two solutions (up and down), take the second one
    except:
        tF = solve(r[1], t)[0]  # If there's only one solution, take that

    # Horizontal distance traveled when hitting the ground
    xF = r[0].subs(t, tF).evalf()
    
    # Return results
    return r, v, tM, yM, xF, tF
