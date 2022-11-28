import re
file = open('grades.txt' , 'r' , encoding='utf-8')

file_read = file.read()
avg = 0
names = re.findall('[0-9]', file_read)
fixednum = []
number = str()
for i in range(0, len(names)- 1, 2):
    number = names[i] + "." + names[i+1]
    fixednum.append(float(number))
    avg += float(number)
print(fixednum)
print(avg/len(fixednum))
