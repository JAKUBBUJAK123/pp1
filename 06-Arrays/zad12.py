arr = [[2,5,4], [9,0,3]]
print(arr)
print(f"rows: {len(arr)}, columns: {len(arr[1])}")
print(arr[1][1])
print(arr[0][2])
print(arr[1][0:])
for i in arr:
    for row in i :
        print(row , end=" ")
    print(" ")

print(arr[0][2])
print(arr[1][2])
