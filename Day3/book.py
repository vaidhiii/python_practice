class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")


book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Atomic Habits", "James Clear")
book1.display_details()
print()
book2.display_details()