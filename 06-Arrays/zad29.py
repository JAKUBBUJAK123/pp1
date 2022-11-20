arr = [6,8,3,1,0,5,7]

num = int(input('podaj liczbę: '))
ilosc = 0
for i in range(len(arr)):
    if arr[i] > num :
        ilosc +=1

print(ilosc)