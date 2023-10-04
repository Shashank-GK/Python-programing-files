name=input("Enter your name: \n")
age=int(input("Enter your age: \n"))

print("Hello {0} you are {1} years old.".format(name , str(age)))
print("_______________________________________________________________________")
n=int(input("To Know that are you eligible for voting are not press 1 \n "))
print()
if n==1:
    print("Ok Please wait and I make you to know are you eligible or not \n")
    print("_______________________________________________________________________")
    if age >= 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
else:
    print("You had entered northing ")
    print("Please try again ")
