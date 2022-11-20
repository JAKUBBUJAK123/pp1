arr = [6,8,3,1,0,5,7]
def even(array):
    arr2 = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            arr2.append(array[i])
    for j in range(len(array)):
        if array[j]%2 != 0:
            arr2.append(array[j])
    return arr2

print(even([6,8,3,1,0,5,7]))