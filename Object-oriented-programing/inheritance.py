# This program calculates the Area, parameter of rectangle and volume, lid area, total surface area of a cuboid using OOP


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def Area(self):
        return self.length * self.breadth

    def Perimeter(self):
        return 2 * (self.length + self.breadth)

    @staticmethod
    def isSquare(len, bre):
        if len == bre:
            return "Square"
        else:
            return "Not a Square"


class Cuboid(
    Rectangle
):  # The 'Cuboid' class will inherit parameters from 'Rectangle' class
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height

    def lid_area(self):
        return self.length * self.breadth

    def total_surface_area(self):
        return 2 * (
            self.length * self.breadth
            + self.length * self.height
            + self.breadth * self.height
        )


print("\nRectangle parameters: \n")
Length = float(input("Enter the value of length: "))
Breadth = float(input("Enter the value of Breadth: "))
R1 = Rectangle(Length, Breadth)
print(
    "The area for rectangle of dimensions '{0}' and '{1}' is '{2}' .units".format(
        str(Length), str(Breadth), str(R1.Area())
    ),
)
print(
    "The perimeter for rectangle of dimensions {0}' and '{1}' is '{2}' and {3} .units".format(
        str(Length), str(Breadth), str(R1.Perimeter()), R1.isSquare(Length, Breadth)
    )
)

print("\nCuboid parameters: \n")
Length = float(input("Enter the length of the cuboid: "))
Breadth = float(input("Enter the breadth of the cuboid: "))
Height = float(input("Enter the height of the cuboid: "))

c1 = Cuboid(Length, Breadth, Height)

print("\nThe volume of the cuboid is: ", c1.volume(), " .units")
print("The lid area of the cuboid is: ", c1.lid_area(), " .units")
print("The total surface area of the cuboid is: ", c1.total_surface_area(), " .units")
