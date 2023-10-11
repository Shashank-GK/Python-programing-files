# This program will illustrate about the Lambda Functions:
def miles2km(miles):
    kms = 1.6 * miles
    return kms


Miles = float(input("Enter the total Miles to convert it into kilometer "))
print(miles2km(Miles), "Kms")

# The above program can be written as Lambda Function like this:
KM = lambda miles: 1.6 * miles
print(KM(Miles), "Kms")
