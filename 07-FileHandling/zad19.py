import random
file = open('intiger.txt' , 'w')



for i in range(random.randint(1,50)):
    num = random.randint(1,50)

    string = str(num)
    file.write(string)
    file.write("\n")

file.close()