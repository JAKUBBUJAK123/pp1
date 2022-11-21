file = open('numbers.txt' , 'r' , encoding= 'utf-8')



sum = 0
for line in file:
    line = int(line)
    sum += line

print(sum)

file.close()