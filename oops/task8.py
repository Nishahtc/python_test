class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_get(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Price:${self.price:.2f}")
book1 = Book("To Kill a Mockingbird", "Harper Lee", 10.99)
book2 = Book("1984", "George Orwell", 8.99)

print("Book 1 detail:")
book1.display_get()
print("Book 2 detail:")
book2.display_get()
                