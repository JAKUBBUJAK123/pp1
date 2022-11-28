import re
def f(first_letter,last_letter):
    file = open('test.txt', 'r' , encoding="utf-8")
    file_r = file.read()
    first_l = re.findall(r'\b[a-zA-Z]', file_r)
    last_l = re.findall(r'[a-zA-Z]\b' , file_r)
    countfirst = 0
    countlast = 0

    
    for i in range(len(first_l)):
        if first_l[i] == first_letter:
            countfirst += 1
    for j in range(len(last_l)):
        if last_l[j] == last_letter:
            countlast += 1

    file.close()
    return countfirst, countlast

       
   
    
    
print(f('w','d'))