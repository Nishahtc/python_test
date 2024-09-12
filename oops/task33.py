class Student:
    name=input("enter student name:")
    address=input("enter student address:")
    mobile_no=int(input("enter student mobile_no:"))
    def data(cls):
        print(f"student name is {cls.name}")
        print(f"student address is {cls.address}")
        print(f"student name is {cls.mobile_no}")
obj=Student() 
obj.data()       