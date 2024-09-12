class StudentRecord:
    def __init__(self,id= 0,name="",age=0,mobile_no=0):
        self.id=id
        self.name=name
        self.age=age
        self.mobile_no=mobile_no

    def display(self):
        self.id=int(input("enter student id:"))
        self.name=(input("enter student name:"))
        self.age=int(input("enter student age:"))
        self.mobile_no=int(input("enter student mobile_no:"))
          
    
    
data=StudentRecord()
data.display()
print(data.__dict__)

