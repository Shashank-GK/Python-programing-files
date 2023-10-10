a = int(input("Enter the Starting value 'a': "))
d = int(input("Enter the Common difference value 'd': "))
n = int(input("Enter the total term value required value 'n': "))

term = a
s = (n * 2) + a
for i in range(a, s, d):
    print(str(term))
    term = term + d
