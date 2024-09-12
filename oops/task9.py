class Book:
    def __init__(self, tile,author,price):
        self.titles=tile
        self.authors=author
        self.prices=price
    def display_get(self):
        print(f"Title:{self.titles}") 
        print(f"Author:{self.authors}")
        print(f"price:{self.prices:}")
book1=Book("spoken english","Nisha",100) 
book2=Book("gramer","nish", 99)
print("Book 1 detail:")
book1.display_get()
print("Book 2 detail:")
book2.display_get()
