class Person:
    name=input("enter name:")
    age =int(input("enter age:"))
    def greet(self):
        print(f"Hello  i am {self.name}!")
        print(f" i am {self.age} years old!")
on=Person()  
print(on.greet())      