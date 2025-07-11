n=10001    #nth prime
primes=[2]     #array of primes
num = 3  #holds the next num to check
while len(primes)<n:   #stops if we have found the nth number
    isPrime=True  #assume num is a prime
    for i in primes:  
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
    num+=2

print(primes[-1])