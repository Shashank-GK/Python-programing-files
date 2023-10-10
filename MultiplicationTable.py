n = int(input("Enter the number to get it's multiplication table: \n"))
m = int(input("Enter the number to limit multiplication table: \n "))
count = 1
while count < m + 1:
    print(" ", n, " X ", count, " = " + str(n * count))
    count = count + 1

print(" ************************************* ")
# we use the for loop for this same operation :
n1 = int(input("Enter an another number to get it's multiplication table: \n"))
m1 = int(input("Enter the number to limit multiplication table: \n "))
x = m1 + 1
for count in range(1, x):
    print(" ", n1, " X ", count, " = " + str(n1 * count))
