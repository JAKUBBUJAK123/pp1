arr = [5,1,9,6,1]

max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
for j in range(len(arr)):
    if min > arr[j]:
        min = arr[j]


print(max-min)