arr = [15,8,31,47,2,19]
revarr = []
print(f'existed array: {arr}')
i = len(arr)
j = 0
while i > 0 :
    revarr.append(arr[i - 1])
    i -= 1

print(f'reverse array: {revarr}') 