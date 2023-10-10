list = [1, 2, 3, 4, 5, 6, 7, 8]

# indexing and slicing:
print("\n Indexing :")
print(list[1])  # indeximg
print(list[-5])

list[5] = 10  # for writing into list
print("\n Slicing")
list[0:4] = [10, 20, 30]  # slicing
print(list)

x = list[5]  # for reading from list
print(x)

# cconcatenation
print("\n Concatenation:")
list1 = [1, 2, 3]
list2 = [3, 2, 1] + list
list3 = list1 + list2
print(list3)

# iteration
print("\n Iteration:")
for x in list3:  # for i i range (len(list3)):
    print(x)
# Removing the element
print("\n  Removing the element: ")
print(list3.pop(0))  # POP operation
print(list3.pop(1))

print(list3.remove(2))  # removing the element
# list3[:]=[ ]
# Empty list

# indexing and sorting
print("\n indexing: ")
print(list3.index(2))
