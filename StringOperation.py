s=input("Enter the your name: \n")

# Concatenation.
s1='Welcome '+s
print(s1)

# Indexing 
for i in range(0,len(s)):
    print(s[i])

# Repetition
s=s*3
print(s)

# Slicing
s[0:len(s):1] # or s[:len(s):1] or s[::1]
print(s)

# in not and in
print('Welcome' not in s1)

# String Methods 
print(s1.find('W'))
print(s1.find('Welcome ')) # searching from left side

print(s1.rfind('Welcome ')) # searching starts from right side. (s1.rfind('Welcome ',0,15))
print(s1.index('l'))
print(s1.count('l'))

Str='..   .....   @@@  Hai '
# removing spaces.
print(Str.ljust((10),'*') )  # print(Str.rjust(10)) , 
print(Str.center((10),'@') )

print(Str.lstrip()) # print(Str.rstrip()) , print(Str.strip())
print(Str.lstrip('. @'))

# Capitalizing
sa=' Hello'
print(sa.capitalize()) 
print(sa.lower()) 
print(sa.upper())
print(sa.title())
print(sa.swapcase())