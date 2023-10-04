name=input("Enter your name \n")
age=int(input("Enter your age: \n"))

if 18<=age<=31:
    print("****************************************************************************************************************")
    print("Welcome to holiday club {0} ".format(name))
    print("You can register your name for getting subscription in the club \n")
    reg=int(input("Enter 1 to register for the club or 0 to exit this application : \n"))
    if reg==1:
        n1=input("Enter your name \n")
        phNo=input("Enter the phone number \n")
        email=input("Enter your email \n")
        print("******************************************************************************************************************")
        
        sub=int(input("I"))
        print("Thank you {0} for joining the club".format(n1))
    else:
        print("Thank you for showing the interest in the club  \n")
else:
   print("I'm sorry, this club is meet for people whose age is between 18 to 31 \n")