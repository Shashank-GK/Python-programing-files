import math

r = float(input("ENter the radius of Circle: \n"))
if r >= 1:
    a = math.pi * (r * r)
    print("The area of circle with radius ", r, ".units is ", a, " .units")
else:
    print("The measurement cannot be defined in negative numbers ")
    print("Try again")
