def quickSort(items):
    finalList=[]
    middle=len(items)//2
    left=items[:middle]
    pivot=items[middle]
    right=items[middle+1:]
    finalList.append(left)
    finalList.append(pivot)
    finalList.append(right)
    
    return finalList
    
    

list=['b','d','a','c','e']
print(quickSort(list))