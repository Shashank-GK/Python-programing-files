# Dictionary data type
dict1={'apple':'Fruit','tomato':'Vegetable','Orange':'Fruit'}

#Dictionary Comprehensions

print(type(dict1)) #Checking Data type
print(dict1['apple'])
dict1['Carrot']='Vegetable' #Adding the Elements to dictionary
dict1['Mango']='fruit' #changing value for a key
del dict1['apple'] #deleting the element from the dictionary
for i in dict1:          #traversing through dict1
    print(i,",",dict1[i])

for x in range (1,6): # inserting elements using for loop
    dict1[x]=x**2
print(dict1)

dict2=dict(((1,2),(3,4),(4,5))) #creating the Dictionary using iterables (Ex: tuples)
print(dict2)

dict3=dict(([1,2],[3,4],[4,5])) #creating the Dictionary using iterables (Ex: lists)
print("Dict3",dict3)

l1=[1,2,3,4,5,6] #Zipping the two iterables into Dictionary
l2=['A','b','c','d','e']
dict4=dict(zip(l1,l2))
print(dict4)

dict5=dict(enumerate(l2)) # creating the dictionary using 'enumerate' keyword using lis l1
print(dict5)

dict6={x:x+2 for x in range(1,10)}
print(dict6)

dic6=((x,x+2) for x in range(1,10))
print(dict6)

for x,y in enumerate(l2):
    print(x,y)

#Dictionary Looping

dict7={x:y for x,y in enumerate(l2)}
print(dict7)

dict7=dict((x,y) for x,y in enumerate(l2))
print(dict7)

print(dict7.keys(),"",dict7.values(),"",dict7.items())

# Dictionary Methods
dictA={1:'Alpha Romeo',2:'BMW',3:'Chevrolet',4:'Dodge',5:'Endeavour',6:'Ferrari'}
dictB=dictA.copy()
print("Dictionary A :",dictA, "\nDictionary B :",dictB)

dictC={7:'Gemera',8:'Honda'}
dictA.update(dictC)
print(dictA)
