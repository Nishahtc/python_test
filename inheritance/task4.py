class Animal:
    def __init__(self, species):
        self.species = species
        self.age = 0

    def grow(self):
        self.age += 1

class Dog(Animal):
    def __init__(self, name):
        self.name = name

# Creating an instance of Dog
dog = Dog("Buddy")

# Trying to access attributes from Animal class
print(dog.species)  # AttributeError: 'Dog' object has no attribute 'species'
print(dog.age)  # AttributeError: 'Dog' object has no attribute 'age'