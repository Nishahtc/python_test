class Student:
    name=""
    age=0
    mobile_no=0
    @staticmethod
    def input():
        name=input("enter student name:")
        age=int(input("enter student age:"))
        mobile_no=int(input("enter student mobile_no:"))
        return name,age,mobile_no
    @staticmethod
    def display():
        print("student name {name}")  
        print("student age {age}")  
        print("student mobile_no {mobile_no}")  
obj=Student() 
   
# Call the input() static method to get student details
student_name, student_age, student_mobile_no = obj.input()

# Call the display() static method to display the student details
obj.display(student_name, student_age, student_mobile_no)  
         
         


