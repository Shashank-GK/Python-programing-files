Admin=input("Enter your name \n")
n=int(input("Press 1 to check that you have the admin access to this system \n"))
if(n==1):
    if (Admin=='Shashank' or Admin=='Shashank GK'):
        print("You have an Admin Access to this system")
    else:
        print("You don't have admin access to this device \a")