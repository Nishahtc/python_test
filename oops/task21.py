class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))  

    def greet(self):
        print(f"Hello, I am {self.name}!")
        print(f"I am {self.age} years old!")


p1 = Person()
p1.greet()