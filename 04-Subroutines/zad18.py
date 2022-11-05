def sum(n):
    A = str(n)
    i = 0
    B = 0
    while i < len(A):
        B += int(A[i])
        i += 1
    print(B)
sum(7182)