def convert(arr):
    arr1 = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr1.append(arr[i][j])
    return arr1


print(convert([[5,0,3,7,5],[9,0,9,1,2]]))