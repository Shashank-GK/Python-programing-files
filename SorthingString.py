# Sorting Challenge:
s = input("Enter the the string: ")
print(sorted(s))
print(" ".join(s))

# Displaying the data :
item = input("Enter the item: ")
price = input("Enter the prise of the item: ")
t_length = len(item) + len(price)
print(t_length)
dots = "." * (25 - t_length)
print(item + dots + price)
