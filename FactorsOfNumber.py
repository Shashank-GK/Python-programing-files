n=int(input("Enter the number to find its factor: \n"))
print("The factors of the number {0} is : ".format(str(n)))
for i in range(1,n+1):
    if n%i==0:
        print(i)