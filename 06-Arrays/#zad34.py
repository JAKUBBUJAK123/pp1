arr1 = [1,5,12,18,16]

arr2 = [1,2,3,4,5,6,10,12,16,18]

arr3 = []

i = 0
k = 0
while i < 5:
    if arr2[k] == arr1[i]:
        arr3.append(arr2[k])
        i += 1
    else:
        k += 1
        if k > 9 :
            k = 0
            i += 1
arr1.sort
arr3.sort
if arr1 == arr3:
    print(True)

else:
    print(False)
