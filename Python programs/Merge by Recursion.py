def mergeSort(items):
    print("Splitting ",items)
    if len(items)>1: #checks if list is not empty or only 1 item
        mid=len(items)//2 #uses mid point to split the list inti two
        lefthalf=items[:mid]
        righthalf=items[mid:]
        mergeSort(lefthalf) #each recursive call will have atleast one item
        mergeSort(righthalf)
        i=0 #points to the smallest item in list1
        j=0#points to the smallest item in list2
        k=0#points next free space in the list items

        while i < len(lefthalf) and j <len(righthalf): #loops until i and j counters reach the end of a list
            if lefthalf[i]<righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1
        while i <len(lefthalf): #assigns the rest of the leftover items in the left half
            items[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf): #assigns the rest of the leftover items in the right half
            items[k]=righthalf[j]
            j=j+1
            k=k+1

items = ["Florida","Georgia","Delaware","Alabama","California"]
mergeSort(items)
print(items)