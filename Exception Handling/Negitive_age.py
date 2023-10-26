# This program will raise an exception if the user enters a negative number for age.


def Stage(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            print("Your age is", age)
    except ValueError as e:
        print(e)


Age = int(input("Enter your age: "))
print(Stage(Age))
