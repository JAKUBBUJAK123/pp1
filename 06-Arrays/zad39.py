arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print(arr)
a = len(arr) - 1
b = len(arr[0])

#funkcja

jeden = 1
dwa = 2
trzy = 3
cztery = 4
piec = 5

while a >= 0 :
    for k in range(b):
        arr[4][k] = piec
        piec += 5
    a =- 1
    for l in range(b):
        arr[3][l] = cztery
        cztery += 4
    a =- 1
    for m in range(b):
        arr[2][m] = trzy
        trzy += 3
    a =- 1
    for i in range(b):
        arr[0][i] = jeden
        jeden += 1
    for j in range(b):
        arr[1][j] = dwa
        dwa += 2


print(arr)