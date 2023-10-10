# This program will demonstrate the use of closure function


def closureFunction():
    def innerFunction(msg):  # Add msg as an argument to innerFunction
        print("*" * 10)
        print("Hello ", msg)
        print("*" * 10)

    return innerFunction


msg = input("Enter your name: ")
function = closureFunction()
print(
    function(msg)
)  # Call closureFunction and pass msg as an argument to innerFunction
