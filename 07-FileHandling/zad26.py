import re

file = open('longtext.txt' , 'r' , encoding='utf-8')
read_text = file.read()
words = re.findall('[a-zA-Z]{6,}' ,read_text )

for i in range(len(words)):
    print(words[i])
    print(" ")
file.close()
