class Student:
    collage="indixpert"
    def __init__(self,name,marks,age) :
        self.name=name
        self.marks=marks
        self.age=age
        print("add new student")
    def welcome(self) :
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks


s1=Student("Nisha",90, 19) 
print(s1.name,s1.marks,s1.age )   
s2=Student("pari", 91, 19)    
print(s2.name,s2.marks,s2.age)
print(Student.collage)
s1.welcome()
print(s1.get_marks())