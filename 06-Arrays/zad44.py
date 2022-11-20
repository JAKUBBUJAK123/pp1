def matrix(n,m):
    arr = []
    a = 1
    for i in range(n):
        arr.append([0 for i in range(m)])
        for j in range(m):
            arr[i][j] = a
            a += 1
            if a == 10:
                a = 0
    return arr

print(matrix(3,5))