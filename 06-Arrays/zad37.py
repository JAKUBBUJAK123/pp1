arr = [[7,3,9,7,0],[2,9,0,1,5],[3,8,6,4,7],[8,7,1,1,5]]

sum = 0
a = len(arr)- 1
b = len(arr[a])
for i in range(b):
    sum += arr[a][i]

print(a,b, sum)