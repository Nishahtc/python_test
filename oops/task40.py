class data:
    def __init__(self):
        self.name=input("enter student name:")
        self.age=int(input("enter student age:"))
    def display(self):
        print(f"student name:={self.name}")
        print(f"student age:={self.age}")

obj=data()        
print(obj.display())