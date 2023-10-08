# Here the calculator.py has function Calculator, where I am importing that function in python program
import calculator as c

A = float(input("Enter the first number: \n"))
B = float(input("Enter the Second number: \n"))
print("Enter 1 for addition: ")
print("Enter 2 for subtraction: ")
print("Enter 3 for Multiplication: ")
print("Enter 4 for division: \n")
Choice = int(input("Enter the choice number : \n"))

print(c.Calculator(A, B, Choice))
