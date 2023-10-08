# Python program to find the factorial of number n:
# Here function will call it self called as Recursive Function


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


N = int(input("Enter the number to find its Factorial: "))

if N == 0:
    print("Factorial of 0 is 1")
elif N < 0:
    print("Factorial does not exist for negative numbers")
else:
    result = fact(N)
    print(f"The factorial of {N} is: {result}")
