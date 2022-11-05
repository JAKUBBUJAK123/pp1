def power(x,n):

    if x == 0 or x == 1 :
        return 1
    if n == 0 :
        return 1
    if n > 0 :
        return x * power(x,n-1)
    
print(power(5,3))