import math
a = int(input("Enter the 1st co-efficient of quadratic equation: \n"))
b = int(input("Enter the 2nd co-efficient of quadratic equation: \n"))
c = int(input("Enter the 3rd co-efficient of quadratic equation: \n"))

disc = b*b - 4*a*c

if a == 0 and b == 0:
    print("{0},{1},{2} Invalid inputs".format(a, b, c))
elif a == 0:
    print("Linear Equation ")
    root1 = -c/b
    print("The Root is: ", root1)
elif disc == 0:
    print("ROOTS ARE REAL AND EQUAL:")
    root1 = -b/(2*a)
    root2 = -b/(2*a)
    print("The {0} is the 1st root and {1} is the 2nd root:".format(root1, root2))
elif disc > 0:
    print("ROOTS ARE REAL AND DISTINCT:")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print("The {0} is the 1st root and {1} is the 2nd root:".format(root1, root2))
else:
    print("ROOTS ARE IMAGINARY:")
    real = -b/(2*a)
    imaginary = math.sqrt(abs(disc))/(2*a)
    print("The ( {0} + {1} i) is the 1st root and ( {0} - {1} i )is the 2nd root:".format(real, imaginary))