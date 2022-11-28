def f(age):
    dogage = 20
    i = 0
    if age == 1:
        return 10
    elif age == 2:
        return 20
    else:
        for i in range(age - 2) :
            dogage +=4
            

        return dogage


print(f(15))
