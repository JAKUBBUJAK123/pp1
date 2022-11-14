arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
lenght = len(arr[0])
name = arr[0]
for i in range(len(arr)):
    if lenght < len(arr[i]):
        lenght = len(arr[i])
        name = arr[i]

print(name)