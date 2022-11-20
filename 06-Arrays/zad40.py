arr = [[-38,19],[5,40],[-7,11],[29,16]]

maxn = arr[0][0]
minn = arr[0][0]
location_a = "0 0"
location_b = "0 0" 

print(maxn , minn)

for i in range(len(arr)):
    for j in range(2):
        if maxn < arr[i][j]:
            maxn = arr[i][j]
            location_a = str(i) + " " + str(j) 
        if minn > arr[i][j]:
            minn = arr[i][j]
            
        

print(maxn, location_a, minn)
print(location_b)