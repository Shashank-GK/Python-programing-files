n = int(input("Enter the number:\n"))
m = n
sum = 0
while n > 0:
    r = n % 10
    n = n / 10
    sum = sum + (r * r * r)
if sum == m:
    print("It is an Armstrong number \n")
else:
    print("It is not an Armstrong number \n")
