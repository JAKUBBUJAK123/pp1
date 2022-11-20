def create_2d_arr(x,y):
    arr = []
    for i in range(x):
        arr.append([0 for j in range(y)])
        
    return arr
    
print(create_2d_arr(3,6))