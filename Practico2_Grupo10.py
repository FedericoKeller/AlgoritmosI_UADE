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

def createRotation(currentOdd, trib):
    resp = []

    for num in trib:
        if(currentOdd >= num):
            resp.append(num)

    
    return resp


def isDivisible(current_rotation):
    resp = []
    for rotation in current_rotation:  
        resp.append(rotation[0] % rotation[1] != 0)
    
    return all(resp)


def createDictionary(trib, odd):
    trib_dict = {}

    resp = []
    current_rotation = []

    for o in odd:
        for n in createRotation(o, trib):
            current_rotation.append([o, n])
            resp.append(o % n != 0)
        

        if(isDivisible(current_rotation)):
            trib_dict[current_rotation[-1][1]] = o
        
        current_rotation = []
    

    print(trib_dict)
        


   
    
 
        
n = 14
trib = getTrib(n)
filteredTrib = list(filter(lambda trib_elem: trib_elem != 1, trib))

odd = getOddNumbers(14)


createDictionary(filteredTrib, odd)