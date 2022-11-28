a = str(input("podaj nazwę pliku: "))
file = open( a , 'r' , encoding='utf-8')
sum = 0
b = 0
for i in file:
    sum = len(i)
    b += 1
    

print(f"nazwa pliku: {a} , ilość wierszy:{b}")


