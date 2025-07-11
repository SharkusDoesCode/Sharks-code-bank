def prime_factors(n):
    factors = []
    for i in range(2,n-1):
        if n%i==0:
            factors.append(i)
            if len(prime_factors(i))>0:
                factors.remove(i)
            print(i)
    return factors



print(prime_factors(8885143))
    