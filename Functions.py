# Writing the function

def sum(a,b):
    result=a+b
    return result

N1=float(input('Enter the 1st number:'))
N2=float(input('Enter the 2nd number:'))

print(sum(N1,N2))

# Calculating the net sealery of an employs

def net_sal(basic,allowance,deduction):
    net=basic+allowance-deduction
    return net

basic_Sealery=float(input('Enter the basic sealery of employ: '))
Allowance=float(input('Enter the allowance: '))
Deduction=float(input('Enter the amount of deduction: '))

print('Your net sealery is ',net_sal(basic_Sealery,Allowance,Deduction))