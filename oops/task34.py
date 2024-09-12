class Student:
    # Class variables to hold student data
    name = ""
    address = ""
    mobile_no = 0

    @classmethod
    def input_data(cls):
        cls.name = input("Enter student name: ")
        cls.address = input("Enter student address: ")
        cls.mobile_no = int(input("Enter student mobile number: "))

    @classmethod
    def display_data(cls):
        print(f"Student name is: {cls.name}")
        print(f"Student address is: {cls.address}")
        print(f"Student mobile number is: {cls.mobile_no}")

# Create an instance of the Student class
obj = Student()

# Input student data
obj.input_data()
# Display student data
obj.display_data()