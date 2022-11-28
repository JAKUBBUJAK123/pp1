file1 = open('longtext.txt' , 'r')

file2 = open('copy.txt' , 'w')

copy = file1.read()

file2.write(copy)

file1.close()
file2.close()

