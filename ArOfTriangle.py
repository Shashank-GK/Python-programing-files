print("This program is meet for finding area of triangle using height and base ")
base = int(input("Enter the value of base \n"))
height = int(input("Enter the value of height \n"))
if base >= 0 and height >= 0:
    (area) = (base * height) / 2
    print("The area of the rectangle is : " + str(area) + " units")
else:
    print("Invalid input")
    print("Measurements cannot be defined in negative number ")

print("***************************************************************************")

print(
    "This program is meet to find the area of triangle using the sides of triangle \n"
)

a = int(input("Enter the value of side a \n"))
b = int(input("Enter the value ofm side b \n"))
c = int(input("Enter the value of side c \n"))

if a >= 0 and b >= 0 and c >= 0:
    s = (a + b + c) / 2
    area2 = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The area of the triangle is : " + str(area2) + " units")
    print("the semi perimeter of triangle is: " + str(s) + " Units")
else:
    print("Invalid input ")
    print("Measurements cannot be defined in negative number ")
