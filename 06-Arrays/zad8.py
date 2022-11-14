arr = [-15, 8, -31, 47, -2, 19]

Vmax = arr[0]
Vmin = arr[0]

for i in range(len(arr)):
    if arr[i] > Vmax:
        Vmax = arr[i]
    elif arr[i] < Vmin:
        Vmin = arr[i]

print(f"Vmax = {Vmax}, Vmin = {Vmin}")
