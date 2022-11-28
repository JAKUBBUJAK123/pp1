file1 = open('GrainsAndBread.txt' , 'r')
file2 = open("MeatAndFish.txt" , 'r')
file3 = open('shoppinglist.txt' , 'w')

for line in file1:
    file3.write(line)
    file3.write('\n')
for anotherline in file2:
    file3.write(anotherline)
    file3.write('\n')

file3.close() 
file1.close()
file2.close()
