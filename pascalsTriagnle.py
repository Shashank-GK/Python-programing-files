# This program will print the Pascal's triangle by taking the row number from the user
def pascal(n):
    r = [1]
    for i in range(n):
        print(r)
        tr = [0] + r
        r = r + [0]
        nr = [x + y for x, y in zip(r, tr)]
        r = nr


N = int(input("Enter the number of rows you want in pascal's triangle : "))
print(pascal(N))
