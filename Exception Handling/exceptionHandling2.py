# Handling Multiple Exceptions

l = [10, 20, 30, 40, 50, 60]

try:
    index = int(input("Enter the index: "))
    print(l[index])
except (IndexError, ValueError) as msg:
    print(msg)
