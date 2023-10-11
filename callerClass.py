# This python program will demonstrate the Caller class function:
def Depts():
    depts = {
        "hr": "Human resource department",
        "sd": "sales and Marketing department",
        "acc": "Accounting department",
        "it": "Information Technology department",
        "pd": "Production department",
    }

    def dname(dept):
        return depts[dept]

    return dname


print(
    "The Departments are as follows: \n hr: Human resource department \n sd: sales and Marketing department \n acc: Accounting department \n it: Information Technology department \n pd: Production department"
)
d = Depts()
a = input("Enter the department code: ")
s = d(a)
print(s)
