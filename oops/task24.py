class Student:
    id=int(input("enter id:-"))
    name=(input("enter name:-"))
    age=int(input("enter age:-"))
    def display(self):
        print(f"student id is {self.id}")
        print(f"student name is {self.name}")
        print(f"student age is {self.age}")
ob=Student()
print(ob.display())