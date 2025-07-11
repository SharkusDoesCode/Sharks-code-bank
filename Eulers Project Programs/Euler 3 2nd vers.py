import math

def maxPFact(n):
    factors = []
    for i in range(2, int(math.sqrt(n))+1):         #loops from 2 to the all possible factors of n
        if n%i == 0:                                #checks if the num/index is cleanly divided - a factor
            x = True                               
            print(i,' is a factor')
            for j in range(2, int(math.sqrt(i))+1): #loops from 2 to all possible factors of the factor(i)
                if i%j == 0:                        #checks if factor/index is cleanly divided - not a prime factor 
                    x = False                       #the factor has its own factors = not prime
                    print(j,'prevents',i,'from being a prime factor')
                    break                           #terminated the for loop to save processing power
                x = True                            #the factor is therefore a prime
            if x:
                factors.append(i)                   #adds factor to list
                print(i,'is a prime factor')
    return max(factors)                             #maximum factor is returned

print(maxPFact(600851475143))