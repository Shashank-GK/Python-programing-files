mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: "))

# Find the maximum of mark1 and mark2
if mark1 > mark2:
    max1 = mark1
else:
    max1 = mark2

# Find the maximum of mark1 and mark3
if mark1 > mark3:
    max2 = mark1
else:
    max2 = mark3

# Find the maximum of mark2 and mark3
if mark2 > mark3:
    max3 = mark2
else:
    max3 = mark3

# Find the average of the best two marks
best_two_avg = (max1 + max2 + max3) / 3

print("The average of the best two marks is:", round(best_two_avg, 2))
