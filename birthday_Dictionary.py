#Dictionary challenge
#Find Birthday of person 

bD={'Roith':'11/11/2002','Rangaswami':'31/5/2002','Ragu':'5/12/2002','Ramesh':'12/12/2002'}
print(bD)

print("Names: Roith, Ramesh, Ragu, Rangaswami")
Name=input("Enter the name to find there Date of birth:")
print(bD.get(Name))
 