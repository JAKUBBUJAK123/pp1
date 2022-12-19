class Student :
    
    id = 10000
    def  __init__(self,name,surname,field):
        self.name = name
        self.surname = surname
        self.id = Student.id 
        self.field = field
        Student.id += 1
         
    def __str__(self) :
        return self.name + " " + self.surname + " " + str(self.id) + " " +self.field


s1 = Student("Anna", "May", "Informatics")
s2 = Student("Jakub" , 'Bujak' , "IT")

print(s1)
print(s2)
        