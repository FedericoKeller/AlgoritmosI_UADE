



def getTrib(n):
    trib = []
    if (n < 1):
        return
  
    first = 1
    second = 1
    third = 1
 
    trib.append(first)
    if (n > 1) :
        trib.append(second)
    if (n > 2) :
        trib.append(second)


    for _ in range(3, n) :
        curr = first + second + third
        first = second
        second = third
        third = curr
 
        trib.append(curr)
    
    return trib
     
def getOddNumbers(n):
    odd = []
    cont = 1
    while (len(odd) < n):
        if(cont % 2 != 0) and cont >= 3:
            odd.append(cont)
        
        cont += 1


    return odd 

def createDictionary(trib, odd):
    for i in range(len(trib)):

        print(trib[i], odd[i])
        


# Driver code
n = 100
trib = getTrib(n)
odd = getOddNumbers(100)


createDictionary(trib, odd)