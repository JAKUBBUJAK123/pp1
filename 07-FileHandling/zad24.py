import re

text ='To be, or not to be, that is the question'


Cont = re.findall('[aeiou]' , text)

for i in range(len(Cont)):
    i+= 1
print(Cont , i)