arr = [2,3,2,5,8,1,9,8]
arr1 = []
a = False
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            a = True
        else:
            a = False
    if a == True:
        arr1.append(arr[i])            
arr1.pop(0)
arr1.pop(1)
print(arr1)