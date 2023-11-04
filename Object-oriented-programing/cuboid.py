# This program calculates the volume, lid area and total surface area of a cuboid using OOP


class Cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.breadth

    def lid_area(self):
        return self.length * self.breadth

    def total_surface_area(self):
        return 2 * (
            self.length * self.breadth
            + self.length * self.height
            + self.breadth * self.height
        )


Length = float(input("Enter the length of the cuboid: "))
Breadth = float(input("Enter the breadth of the cuboid: "))
Height = float(input("Enter the height of the cuboid: "))

c1 = Cuboid(Length, Breadth, Height)
print("\nThe volume of the cuboid is: ", c1.volume(), " .units")
print("The lid area of the cuboid is: ", c1.lid_area(), " .units")
print("The total surface area of the cuboid is: ", c1.total_surface_area(), " .units")
