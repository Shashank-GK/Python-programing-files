# This Nested Exception on python program will act as calculator

print(" \n", "*" * 10, "Simple Calculator", "*" * 10, "\n")
a = float(input("Enter the first number: \n"))
b = float(input("Enter the Second number: \n"))
print("Enter 1 for addition: ")
print("Enter 2 for subtraction: ")
print("Enter 3 for Multiplication: ")
print("Enter 4 for division: \n")
choice = int(input("Enter the choice number : \n"))

if choice == 1:
    Sum = a + b
    print("{0} is the sum of number {1} and {2}".format(Sum, a, b))
elif choice == 2:
    diff = a - b
    print("{0} is the difference of number {1} and {2}".format(diff, a, b))
elif choice == 3:
    prdt = a * b
    print("{0} is the product of number {1} and {2}".format(prdt, a, b))
elif choice == 4:
    try:
        if b != 0:
            qot = a / b
            print("{0} is the Quotient of number {1} divided by {2}".format(qot, a, b))
        else:
            print("Division by zero is not allowed")
    except ValueError as msg:
        print("Do not insert '0' as second number for division ")
        print("Dividing any number will give Infinity ")
        print(msg)
else choice > 4:
    print("You have entered the wrong choice number: ")
    print("Try again ")
