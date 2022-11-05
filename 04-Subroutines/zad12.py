def Sum(N):

    if N == 0 :
        return 0 
    if N > 0 :
        return N + Sum(N-1) 



x = 10
print(Sum(x))   
