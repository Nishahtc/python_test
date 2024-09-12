class Student:

    name=input("enter student name:")  
    age=int(input("enter student age")) 
    print("add new student:") 
    def display(self) :
        print(f"student name {self.name}") 
        print(f"student age {self.age}") 
obj=Student()  
obj.display()      


