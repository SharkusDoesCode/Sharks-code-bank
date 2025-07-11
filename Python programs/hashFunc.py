url=input('Paste URL')
def hashFunc(url):
    #removes the protocol and www in the URL
    firstDot=url.index('.')
    url=url[firstDot+1:len(url)-1]
    
    #removes the domain name in the URL
    secondDot=url.index('.')
    url=url[0:secondDot]
    url=url.upper()
    print(url)
    
    #hashing function via ascii
    value=0
    for i in range(0,len(url)):
        print(ord(url[i]),url[i])
        value=value+ord(url[i])
    return value
    
print(hashFunc(url))