# This python program will illustrate the Decorator function:
def decorator(fun):
    def Wrapper(msg, name):
        print("*" * 10)
        fun(msg, name)
        print("*" * 10)

    return Wrapper


@decorator
def display(msg, name):
    print(msg, name)


Msg = "Hai"
Name = input("Enter your name:")
# d = decorator(display)
# print(d(Msg,Name))
print(display(Msg, Name))
