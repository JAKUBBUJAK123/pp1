import random
class Array:
    
    @staticmethod
    def create_array(number_of_elements, what_number):
        for i in range(number_of_elements):
            list.append(what_number)          

    @staticmethod
    def random_arr(number,value1,value2):
        for j in range(number):
            list.append(random.randint(value1,value2))

    @staticmethod
    def how_many(min,max):
        return max-min
    
list = []

Array.random_arr(10,2,40)
print(Array.how_many(2,30))
print(list)