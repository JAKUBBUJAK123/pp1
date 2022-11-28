file1 = open('longtext.txt' , 'r' , encoding='utf-8')

file2 = open('copylines.txt' , 'w')
a = str()
for line in file1 :
    
    file2.write(line)


file1.close()
file2.close()