def quickSort(items):
    if len(items) <= 1:
        return items
    else:
        pointer1 = 0
        pointer2 = len(items)-1
        while pointer1 != pointer2:
            if(items[pointer1] > items[pointer2] and 
            pointer1<pointer2) or (items[pointer1] <
            items[pointer2] and pointer1 > pointer2):
                temp=items[pointer1]
                temp = items[pointer1]
                items[pointer1]=items[pointer2]
                items[pointer2]= temp
                temp_pointer=pointer1
                pointer1=pointer2
                pointer2=temp_pointer
            if pointer1<pointer2:
                pointer1=pointer1+1
                print(items)
            else:
                pointer1=pointer1-1
                print(items)
    left=quickSort(items[0:pointer1])
    right=quickSort(items[pointer1+1:len(items)])
    return left+[items[pointer1]]+right

list=['London','Birmingham','Oxford','Luton','Manchester']
print(quickSort(list))
