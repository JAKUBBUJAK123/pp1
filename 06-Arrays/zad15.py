arr = [[0,0,0], [0,0,0], [0,0,0]]

for row in arr:
    for i in row:
        if i == 0 and row - 1== 0 :
            arr[i][row - 1] = 1      
            
        print(i , end=" ")
    print(" ")
