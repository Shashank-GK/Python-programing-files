l=int(input("Enter the length of cuboid: \n"))
b=int(input("Enter the breadth of cuboid: \n"))
h=int(input("Enter the height of cuboid: \n"))
if l>=0 and b>=0 and h>=0:
    area=l*b*h
    print("The area of cuboid is: ",area," units")
    perimeter=2*(l+b+h)
    print("The perimeter of cuboid is: ",perimeter," units")
    volume=l*b*h
    print("The volume of cuboid is: ",volume," units")
else:
    print("invalid Inputs")
    print("Measurements cannot be defined in the negative value ")