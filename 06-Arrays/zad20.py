arr = [12,6,4,9,10]
def star(n):
    num = 0
    for i in range(len(arr)):
        j = arr[i]
        print(" ")
        for k in range(j):
            print("*" , end=" ")
            num += "*"
    return num