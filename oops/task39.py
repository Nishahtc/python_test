class data:
    collage="indixpert"
    name=input("enter student name:")
    age=int(input("enter student age:"))
    marks=int(input("enter student marks:"))
    def display(self):
        print(f"student name {self.name}")
        print(f"student age {self.age}")
        print(f"student marks {self.marks}")
obj=data()  
print(obj.display())
print(obj.collage)      