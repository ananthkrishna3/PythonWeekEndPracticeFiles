dynamiclist= [1,"hello",3.14]
#forward order for retriving elements
print(dynamiclist[0])

#forward order for retriving elements
print(dynamiclist[-1])
#Sorting List
sortList = [8,6,93,41,3,8,80,16,18,20,41,50]
print(sortList)
for n in range(len(sortList)):
    for x in range(len(sortList)):
        if sortList[n] < sortList[x]:
                temp=sortList[n]
                sortList[n]=sortList[x]
                sortList[x] = temp
for m in range(len(sortList)):
    print(sortList[m])

#adding Elements in Lists
ListExample = [1,3,5,7,9]
ListExample.append(1)
ListExample.insert(1,2)
Tuples=(10,11)
ListExample.insert(7,Tuples)
print(ListExample)