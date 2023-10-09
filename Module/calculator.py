# This python program will act as Simple calculator and imported as module in calculator.py
print(__name__)


def Calculator(a, b, choice):
    if choice == 1:
        Sum = a + b
        return "{0} is the sum of number {1} and {2}".format(Sum, a, b)
    elif choice == 2:
        diff = a - b
        return "{0} is the difference of number {1} and {2}".format(diff, a, b)
    elif choice == 3:
        prdt = a * b
        return "{0} is the product of number {1} and {2}".format(prdt, a, b)
    elif choice == 4:
        qot = a / b
        return "{0} is the Quotient of number {1} divided by {2}".format(qot, a, b)
    elif choice >> 4:
        return "You have entered the wrong choice number: "
        return "Try again "
