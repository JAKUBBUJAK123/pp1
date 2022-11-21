import random
file = open('randint' , 'w' , encoding="utf-8")

for i in range(50):
    a = str(random.randint(100,999))
    file.write(a)
    file.write("\n")
file.close()