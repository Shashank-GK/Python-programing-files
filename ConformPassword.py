p1=input("Enter the Password: ")
p2=input("Conform The password: ")

if(p1==p2):
    print("Password is Correct")
else:
    if p1.casefold()==p2.casefold():
        print("Please check the cases and try again ")
    else:
        print("The passwords you entered are not matching ")
        print("Please Try Again")
