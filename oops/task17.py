class Person:
    def __init__(self, name: str, age: int):
        """Initialize the Person object with name and age."""
        self.name = name
        self.age = age

    def greet(self):
        """Print a greeting message using the person's name."""
        print(f"Hello, my name is {self.name}!")

# Create an object of the Person class with sample data
person1 = Person(name="Alice", age=30)

# Call the greet method
person1.greet()