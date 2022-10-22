num1 = int(input("first num: "))
num2 = int(input("first num: "))

if num1 > 0 and num2 > 0 :
    print(f"point P({num1},{num2}) is in the first quadrant")
elif num1 < 0 and num2 > 0 :
    print(f"point P({num1},{num2}) is in the second quadrant")
elif num1 <0 and num2 <0 :
    print(f"point P({num1},{num2}) is in the third quadrant")
elif num1 > 0 and num2 < 0 :
    print(f"point P({num1},{num2}) is in the fourth quadrant")