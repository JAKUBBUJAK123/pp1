def calc ():
    #s = 2 h= 2 a= 1 r = 2 p= 1 o =2 t = 1 e= 1
    s = 0
    h= 0
    a = 0
    r = 0
    p = 0
    i = 0 
    while i < len(calc()):
        if calc[i] == 's':
            s += 1 
            i += 1
        else:
            i+= 1
        if calc[i] == 'h':
            h += 1 
            i += 1
        else:
            i+= 1
        if calc[i] == 'a':
            a += 1 
            i += 1
        else:
            i+= 1
        if calc[i] == 'r':
            r += 1 
            i += 1
        else:
            i+= 1
        if calc[i] == 'p':
            p += 1 
            i += 1
        else:
            i+= 1
        
    print(f"s:{s} a:{a} r:{r} p:{p} h:{h}")

calc("sharpshooter")