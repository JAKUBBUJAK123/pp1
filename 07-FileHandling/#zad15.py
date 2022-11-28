file = open('longtext.txt' , 'r' , encoding='utf-8')
j = 0

for i in file :
    print(i)
    j += 1
    if j//5 == 0 and j != 0 :
        input('press enter')
        j = 0


file.close()
