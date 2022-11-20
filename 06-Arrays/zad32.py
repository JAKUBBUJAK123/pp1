def func (arr):
    string = ''
    
    for i in range(len(arr)):
        string += str(arr[i]) + ","

    
    return string

print(func([5,4,3,2,6,5]))