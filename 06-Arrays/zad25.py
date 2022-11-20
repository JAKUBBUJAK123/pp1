def ocurs(number, array):
    
    for i in range(len(array)):
        if array[i] == number :
            a = True
    if a == True :
        return True
    else:
        return False
        
            
print(ocurs(23,[15,38,7,23,14]))
    

