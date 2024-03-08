from function import *
import sys


if len(sys.argv) != 1:
    given = sys.argv
else:
    given = input("Write as [V0] [Launch angle] [Y0 (default is 0)]: ")
    given= given.split(" ")
    given.insert(0,"main.py")
r, v, tM, yM, xF, tF = calc(given)
print(f"Velocity vector: ({v[0].evalf()})i + ({v[1].evalf()})j m/s")
print(f"Position vector: ({r[0].evalf()})i + ({r[1].evalf()})j m")
print(f"Time to reach highest height: {str(tM)} s")
print(f"Highest height: {str(yM)} m")
print(f"Time to reach range: {str(tF)} s")
print(f"Range: {str(xF)} m")