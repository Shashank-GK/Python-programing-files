# Dictionary Challenge
#Adding the countries according to there alphabetic order.

countries={}
totalNumber=int(input('Enter the number of countries you are adding :'))
Range=int(totalNumber)
for i in range(Range):
    name=input('Enter the country name: ')
    if name[0].upper() not in countries:
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)

print(countries)