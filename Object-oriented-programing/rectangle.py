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
