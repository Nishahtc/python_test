class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello i am {self.name}!") 
        print(f"i am {self.age} years old!")    
p1=Person("Nisha", 19)
p1.greet()        