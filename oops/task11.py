class Student:
    def __init__(self,name,age,grade) :
        self.name=name
        self.age=age
        self.grade=grade
        print("add new student")
    def display_info(self):
        print(f"Student name is {self.name}")    
        print(f"Student age is {self.age}")    
        print(f"Student grade is {self.grade}")  
s1=Student("Nisha modi", 19,"90 %")
s1.display_info()  
s2=Student("Khushi keshari", 19,"90 %")
s2.display_info()          