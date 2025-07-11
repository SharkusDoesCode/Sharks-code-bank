def findNonFactor(num):

    for factor in range(2,21): 
        #print(factor)
        if num%factor!=0:
            #print(factor,'not a factor')
            return True  #terminates function and returns True
        #else:
            #print(factor,'is a factor')

    return False   #if num divisible by all factors
        
def Euler5():
    for num in range(100000000,1000000000,20):
        #print(num)
        if findNonFactor(num) == False:
            return num

#main

print('the solution is',Euler5())

                



            
