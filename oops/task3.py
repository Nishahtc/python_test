class Student:
    def __init__(self, fullname):  # Corrected the method name from __init to __init__
        self.name = fullname
        print("Added new student")  # Changed "add" to "Added" for better readability

# Creating an instance of the Student class
s1 = Student("Nisha") 
print(s1.name)  # This will print the name of the student        
        
