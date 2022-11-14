import random
arr = [random.randint(1,100)for i in range (20)]
even = []
odd = []

j = 0
while j < len(arr) - 1 :
    if arr[j] % 2 == 0 :
        even.append(arr[j])
        j += 1
    else :
        odd.append(arr[j])
        j += 1
print(f"even: {even}")
print(f"odd: {odd}")