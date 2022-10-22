fivezl = 0
twozl = 0
onezl = 0
money = int(input("podaj ilosc zł: "))
if money > 5:
    fivezl =    money%5
if fivezl > 2:
    twozl = fivezl%2
if twozl > 0 or fivezl > 0 :
    onezl = 1
print(f"5zł: {fivezl}, 2zł: {twozl}, 1zł: {onezl}")