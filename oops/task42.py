class Student:
    def __init__(self, name="", age=0, mobile_no=0):
        self.name = name
        self.age = age
        self.mobile_no = mobile_no

    def input(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))
        self.mobile_no = int(input("Enter student mobile number: "))

    def display(self):
        print(f"Student Name: {self.name}")  
        print(f"Student Age: {self.age}")  
        print(f"Student Mobile Number: {self.mobile_no}")  

# Create a Student object
students = Student()

# Call the input method to get student details
students.input()

# Call the display method to show student details
students.display()