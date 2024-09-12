class Dog:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(f"domastic dog {self.name}") 
        print(f"price {self.price}") 
d1=Dog("tommy",30000)
d1.display()