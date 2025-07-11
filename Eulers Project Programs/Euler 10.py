import time

start_time = time.time()  # Record the start time

#Number theory approach - Sieve of Eratosthenes
max = 2000000      #Need to find all prime numbers up to 2 million
boolArray= [True]*(max+1)    #Assume all numbers are primes by making a boolean array
n = 2 #The first prime number

while n*n <= max:  #same as n <= sqrt(max), but doesn't use a function
    if boolArray[n]:  #These 2 lines will check every n value up to sqrt(max)

        for i in range(n*n,max+1,n): 
            #loops from n*n(as smaller multiples below n*n are most likely marked as False)
            #loops until 2 million + 1 due to zero indexing
            #with a skip of n so it iterates for every multiple of n

            boolArray[i] = False   #marks all multiples as false as they are not a prime

    n += 1
    while n <= max and not boolArray[n]: #checks if the increment of 1 does not = a prime number
        n += 1     #iterate to next number until the numbers is prime or largest prime

primes = []  #initialsing list to store every prime after each sift
for j in range(2,max+1):   #goes through the every number up to 2 million
    if boolArray[j]: # if the iteration gives a True value
        primes.append(j)

for i in range(1000000):
    pass
end_time = time.time()  # Record the end time

execution_time = end_time - start_time  # Calculate the time taken
print(f"Time taken: {execution_time:.6f} seconds")

print('The summation of every prime up to 2,000,000 is',sum(primes))        