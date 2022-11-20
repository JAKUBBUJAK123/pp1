def bublesort(array):
    a = 0
    b = 0
    while a < 6:
        for i in range(len(array)- 1):
            if array[i] > array[i+1]:
                b = array[i]
                array[i] = array[i+ 1]
                array[i + 1] = b
            
        a += 1
    return array

print(bublesort([8,9,1,4,6,5]))