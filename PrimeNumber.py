n=int(input("Enter the number to check if it is prime number or not: "))
f=False
if n==1:
    print(str(n)+" is not a prime number.")
elif n>1:
    for i in range(2,n):
        if (n%i)==0:
            f=True
            break

    if f:
        print(str(n)+" is not a prime number")
    else:
        print(str(n)+" is a prime number")