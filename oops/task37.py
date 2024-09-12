class Student:
    name="Nisha"

    age=19
obj=Student() 
print(obj.name )  
print(obj.age )
obj2=Student()
print(obj2.name)

class Student:
    name=input("enter name:-")
    age=input("enter age:-")
    def display(self):
        print(f"student name is {self.name}")
        print(f"student age is {self.age}")
obj=Student()
print(obj.display())
class St:
    name=""
    def __init__(self):
        print("add new student:-")
s1=St() 
print(s1.name)
      


