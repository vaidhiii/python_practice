class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")


class Library:

    def __init__(self):
        self.inventory = []

    def add_book(self):
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book=Book(title,author)
        self.inventory.append(book)
        print("Book Added Successfully.")

    def display_books(self):
        if len(self.inventory)==0:
            print("No books available.")
        else:
            print("\n------Available Books------")
            for book in self.inventory:
                book.display_details()
                print()

    def search_book(self, ):
        title=input("Enter book title to search: ")
        for book in self.inventory:
            if book.title.lower()==title.lower():
                print("\nBook Found!")
                book.display_details()
                return
        print("Book Not Found.")

library=Library()

print("......Library Management System......")
while True:
    print("1. Add Book\n2. Display Books\n3. Search Book\n4. Exit")
    try:
        choice = int(input("Enter a Choice: "))
        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            library.search_book()
        elif choice == 4:
            print("Thank you for using Library Management System.")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 to 4")
    except ValueError:
        print("Enter Valid Choice.")
