class Student:
    def __init__(self, name="", age=0, mobile_no=0):
        self.name = name
        self.age = age
        self.mobile_no = mobile_no

    @classmethod
    def input(cls):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        mobile_no = int(input("Enter student mobile number: "))
        return cls(name, age, mobile_no)

    def display(cls):
        print(f"Student Name: {cls.name}")  
        print(f"Student Age: {cls.age}")  
        print(f"Student Mobile Number: {cls.mobile_no}")  

# Create a Student object using the class method
student = Student.input()

# Call the display method to show student details
student.display()