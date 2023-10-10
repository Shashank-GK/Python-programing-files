# Dictionary challenge
# Converting the Roman number into Integer number

roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

numbers = input("Enter the roman number: ")
Numbers = numbers.upper()
deci_num = 0
i = 0
while i < len(Numbers):
    if i + 1 < len(Numbers) and roman[Numbers[i]] < roman[Numbers[i + 1]]:
        deci_num += roman[Numbers[i + 1]] - roman[Numbers[i]]
        i += 2
    else:
        deci_num += roman[Numbers[i]]
        i += 1

print(deci_num)
