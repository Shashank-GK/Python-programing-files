# This python program will illustrate the use of try-except-else block

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))

    c = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Division is: ", c)
