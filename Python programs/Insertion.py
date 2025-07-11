def insertion(list):
    n=len(list)

    for i in range(1,n):   #start value not zero cus index[0] acts as sorted list
        current = list[i]    #holds actual item
        position=i  #holds the current items position
        while position>0 and list[position-1]>current: #checks if: not single item list and prevItem > currentItem
            list[position]=list[position-1]   #swaps items around, overriding current
            position = position-1    #decrements position
        list[position]=current    #if swapped: replaces overrided item with saved current item at new position

    return list
#main

list=[4,5,6,2,8,9,6,1]
sortedList=insertion(list)
print('sorted list', sortedList)

