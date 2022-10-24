import mymath
i = 1
n1 = mymath.read_number()
n2 = mymath.generate_number()

while n1 != n2:
    print("try again")
    n1 = mymath.read_number()
    i += 1
else :
    print(f"you win in {i} try")
    