d = 0
num = 0
count = 0
i = 0
while True :

    num = (input("input number: "))  
    
    if num == 'done':
        break
    else:
        try:
            c = int(num)
            count += c
            i +=1
            avg = count/i
            
            if d < c :
                d = c
            
            
        except:
            print("bad input")
        
print(count, avg, d)
