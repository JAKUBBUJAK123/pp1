def matrix(n):
    arr = []

    for i in range(n):
        arr.append([0 for i in range(n)])
        arr[i][i] = 1
    return arr
print(matrix(3))


