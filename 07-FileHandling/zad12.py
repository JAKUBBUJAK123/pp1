file = open('shoplist.txt' , 'a')

file.write(input("add name of product: "))
file.write('\n')

file.close()