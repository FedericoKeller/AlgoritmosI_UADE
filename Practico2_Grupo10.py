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
    rotation = []

    for num in trib:
        if(currentOdd >= num):
            rotation.append(num)

    
    return rotation


def isNotDivisible(current_rotation):
    hasDivisors = []
    for rotation in current_rotation:  
        hasDivisors.append(rotation[0] % rotation[1] != 0)
    
    return all(hasDivisors)



def getCurrentRotation(number, trib):
    current_rotation = []

    for n_trib in createRotation(number, trib):
        current_rotation.append([number, n_trib])
    

    return current_rotation
    

     


def createDictionary(trib, odd):
    trib_dict = {}
    filteredTrib = list(filter(lambda trib_elem: trib_elem != 1, trib))

    for number in odd:
        current_rotation = getCurrentRotation(number, filteredTrib)

        if(isNotDivisible(current_rotation)):
            trib_dict[current_rotation[-1][1]] = number
        
    

    return trib_dict
        


   
    
def main():
    n = 14
    trib = getTrib(n)
    odd = getOddNumbers(n)

    trib_dict = createDictionary(trib, odd)
    print(trib_dict)


main()