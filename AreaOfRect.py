l = int(input("Enter the value of Length: \n"))
b = int(input("Enter the value of breadth: \n"))
if l >= 0 and b >= 0:
    area = l * b
    print("The area of the rectangle is: ", area, "units")

    perimeter = 2 * (l * b)
    print("The perimeter of the rectangle is: ", perimeter + "units")

    if l == b:
        print("The rectangle is square")
    else:
        print("The rectangle is not a square")
else:
    print("invalid Inputs \n")
    print("Measurements cannot be defined in the negative value ")
