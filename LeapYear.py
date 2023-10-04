year=int(input("Enter the year to check if it is a leap year or not: \n"))
if (year%100==0):
    if(year%400==0):
        print("The {0} year is a leap year ".format(str(year)))
elif (year%4==0):
    print("The {0} is a leap year".format(str(year)))
else:
    print("The {0} is not a leap year ".format(str(year)))