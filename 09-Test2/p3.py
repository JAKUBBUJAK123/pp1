def f(array2D):
    finalar = []
    sum = 0
    a = len(array2D) 
    b = len(array2D[0])
    for i in range(b):
        for j in range(a):
            sum += array2D[j][i]
        finalar.append(sum)
        sum = 0
    return finalar

print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )