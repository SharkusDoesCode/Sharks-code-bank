def merge(list1,list2): #merges two adjacent list together in order
    newList=[] #initialise a list to replace the two
    index1=0 #acts as a pointer for list1
    index2=0 #acts as a pointer for list2
    while index1<len(list1) and index2<len(list2): #loop until one of the pointers has reached the end of the list
        #adds the lowest value between the items indicated by the pointers, the lowest pointer is incremented 
        if list1[index1]>list2[index2]: 
            newList.append(list2[index2])
            index2=index2+1
        elif list1[index1]<list2[index2]:
            newList.append(list1[index1])
            index1=index1+1
        elif list1[index1]==list2[index2]: #appends both items since they are equal
            newList.append(list1[index1])
            newList.append(list2[index2])
            index1=index1+1
            index2=index2+1
    #appends the rest of the items
    if index1<len(list1):
        for item in range(index1,len(list1)):
            newList.append(list1[item])
    elif index2<len(list2):
        for item in range(index2,len(list2)):
            newList.append(list2[item])
    return newList
#main
items=['Florida','Georgia','Delaware','Alabama','California']
listOfItems=[]
item=[]
for n in range(len(items)): #seperates the list into seperate list each containg an item
    item=[items[n]]
    listOfItems.append(item)
while len(listOfItems)!=1: #loops until after every item is in one list
    index=0
    while index<len(listOfItems)-1:
        newList=merge(listOfItems[index],listOfItems[index+1]) #combines items/lists
        listOfItems[index]=newList #assigns the new combined list to index
        del listOfItems[index+1] 
        index=index+1 #basically increments by two since the index+1 is deleted
print(listOfItems[0]) #printed like this to remove the double squared brackets
