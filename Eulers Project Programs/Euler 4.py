#All palindromes with an even number of digits are divisible by 11
def max():
    largest=0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            #assume largest palindrome is 6 digits
            num=str(i*j)
            if (i*j)>=100000:
                if num[0]==num[5] and num[1]==num[4] and num[2]==num[3]:
                    if (i*j)>largest:
                        largest=(i*j)
            else:
                break
    return largest
print(max())


    
