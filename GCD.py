m = int(input("Enter the value of 1st number: \n"))
n = int(input("Enter the value of second number \n"))
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print("The GCD of two numbers is: ", m)
