# This program will illustrate the polymorphism method using duck typing


def Driver(car):
    car.drive()


class BMW:
    def drive(self):
        print("You will be driving BMW M5 CS")


class Porsche:
    def drive(self):
        print("you will be driving Porsche GT3 RS")


CAR = input("Are you willing to drive 'BMW' or 'Porsche': ")
if CAR == "BMW":
    C1 = BMW()
    Driver(C1)
elif CAR == "Porsche":
    C2 = Porsche()
    Driver(C2)
else:
    print("Please confirm the car: ")
