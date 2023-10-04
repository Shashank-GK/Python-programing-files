am=int(input("Enter the total cost of product you brought from our shop to validate discount  : \n"))

if (am<=1000):

    discount=am*10/100

    print("You got a {0} % discount for buy {1} Rs. product from our shop ".format(str(discount),str(am)))

elif(am>1000 and am<=5000):

    discount=am*20/100

    print("You got a {0} % discount for buy {1} Rs. product from our shop ".format(str(discount),str(am)))

elif(am>5000 and am<=10000):

    discount=am*30/100 

    print("You got a {0} % discount for buy {1} Rs. product from our shop ".format(str(discount),str(am)))

elif(am>10000):

    discount=am*40/100

    print("You got a {0} % discount for buy {1} Rs. product from our shop ".format(str(discount),str(am)))

else:

    print("You have not entered the cost.")

    print("please try again.")

dicAmount= (am-discount)
print("You Hav to pay {0}.Rs for having {1} % Discount for buying {2} Rs. value product ".format(str(dicAmount),str(discount),str(am)))



