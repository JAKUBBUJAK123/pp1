arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
arr1 = []

a = len(arr)- 1
x = 0




for i in range(5):
    arr1.append(arr[a][i])

for j in range(5):
    arr[a][j] = arr[0][j]
    arr[0][j] = arr1[j]

print(arr)
print(arr1)