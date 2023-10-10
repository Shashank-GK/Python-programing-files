name = input("Enter your username: \n")
units = int(input("Enter the units consumed: \n"))
metercharge = 100
if units <= 200:
    metercharge = metercharge + (units * 0.08)
elif units > 200 and units <= 300:
    metercharge = metercharge + (units * 0.12)
elif units > 300 and units <= 400:
    metercharge = metercharge + (units * 0.16)
elif metercharge > 400:
    metercharge = metercharge + (units * 0.20)

print(
    "**********************************************************************************\n"
)
print("Name: " + name)
print("The number of units consumed: " + str(units) + ".units")
print("Your meter charge is: " + str(metercharge) + " .Rs")
print(
    "**********************************************************************************\n"
)
print("Thank you ")
