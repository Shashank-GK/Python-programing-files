print("The program is meet to find the fibonacci series of number: \n")
n=int(input("Enter the number of terms: \n"))
a=0
b=1
print(str(a)+ ",")
print(str(b)+ ", ")
for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(str(c)+",")