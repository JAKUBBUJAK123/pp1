import random
arr = [2,3,5,6,4,21,23]

def rand_elem(array):
    a = random.randint(0,len(array)- 1)
    return array[a]




print(rand_elem([2,3,5,6,4,21,23]))