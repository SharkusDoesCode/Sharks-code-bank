#Solution via number theory algorithm   special thanks to Malachy for helping with the maths
#by using primitive pythagorean triples (GCD is 1) 
primPythagTriplets=[
    [3,4,5],
    [5,12,13],
    [7,24,25],
    [8,15,17],
    [9,40,41],
    [11,60,61],
    [12,35,37],
    [13,84,85],
    [15,112,113],
    [16,63,65]
]
#first few primitve pythagorean triplets
#for any positive real value of k: ka^2 + kb^2 = kc^2 is true
found = False
for k in range(1,100):   #using 1 to 10 since any k value larger than 10 for the smallest pythag triplet would be >=1000
    for i in range(len(primPythagTriplets)):  #iterates for all 10 primipythagtriplets
        a = k*primPythagTriplets[i][0]   
        b = k*primPythagTriplets[i][1]
        c = k*primPythagTriplets[i][2]
        total = a + b + c
        print(total)
        if total == 1000:
            print('a+b+c=1000, when a is',a,',b is',b,'and c is',c)
            found = True
            break
    if found:
        print('Therefore, abc =',a*b*c)
        break
            
