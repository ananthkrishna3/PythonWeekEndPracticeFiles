# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:52:35 2019

@author: AnanthKrishna
"""
MyList=["Apple", "orange","Mango", "Banana", "pear", "strawberry", "plums", "Promaganate"]

#printing the Elements of List
print(MyList)

#printing List by index
print(MyList[0])

#changing elements in lists
MyList[-3] = "Blackberry"
print(MyList) 

#Adding Elements using Append
MyList.append("Chikoo")
print(MyList)

#Adding elements at a specified position using Insert
MyList.insert(-1,"WaterMelon")
print(MyList)


#dynamic creation of List
car = []
car.append("Audi")
car.append("Benz")
car.append("BMW")
car.append("Jaguar")
print(car)

#deleting Elements in Lists
car.pop(-1)
print(car)

#Caliculating Length of Lists
print(len(MyList))

#Using for loop to print elements
for items in MyList:
    print(f"{items.title()}, is always sweet")
#for loop using Range    
for x in range(1,10):
    print(x)
    
 # using for range to add numbers into list
numbers=list(range(1,20))
print(numbers) 

#printing even diference between number by providing an extra parameter in range
even_numbers = list(range(2,40,2))
print(even_numbers)

#statistical Operations
print(min(numbers))

print(max(numbers))

#**slicing of lists
print(MyList[3:8])