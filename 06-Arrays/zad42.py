arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

arr1 = []
j = len(arr[0]) - 1
for i in range(3):
    arr1.append(arr[i][0])
    arr[i][0] = arr[i][j]
    arr[i][j] = arr1[i]


print(arr1)
print(arr)
