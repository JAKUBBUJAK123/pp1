
i = 1
pay = 0
Ehours = input("enter hours: ")
try:
    H = float(Ehours)
except:
    print("please write numeric input")
    Ehours = input("enter hours: ")

Erate = input("enter rate: ")
try:
    R = float(Erate)
except:
    print("please write numeric input")
    Erate = input("enter rate: ")

while i <= H :
    if i < 40 :
        pay += R
        i += 1
    else:
        pay += R * 1.5
        i += 1
else: 
    print(pay)
