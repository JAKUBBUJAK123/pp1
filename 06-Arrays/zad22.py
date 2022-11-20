arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
finalarr = []
i = 0
k = 0
while i < 7:
    if arr1[i] != arr2[k]:
        k += 1
        if k == 3:
            finalarr.append(arr1[i])
            i += 1
            k = 0
    else:
        i += 1 
    

        
    
print(finalarr)