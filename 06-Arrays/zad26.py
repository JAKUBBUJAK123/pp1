arr = [5,1,9,6,1]

max = arr[0]
sexmax = arr[1]

for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]

for j in range(len(arr)):
    if sexmax < arr[j] and arr[j] != max :
        sexmax = arr[j]

print(max,sexmax)