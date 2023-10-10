n = int(input("Enter the number to find if it is palindrome or not a palindrome : \n "))
count = 0
sum = 0
m = n
rev = 0
while n > 0:
    count += 1
    r = n % 10
    sum = sum + r
    n = n // 10
    rev = rev * 10 + r

print(" Number of digits are ", count)
print(" Sum of digits is: ", sum)
print(" The reverse of number: ", rev)

if m == rev:
    print(" The Given number {0} is a Palindrome".format(str(m)))
else:
    print(" The Given number {0} is not a Palindrome".format(str(m)))
