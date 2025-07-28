from item import Book, Magazine
from library import Library

library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
magazine1 = Magazine("National Geographic", "National Geographic Society", "2023-01")

library.add_item(book1)
library.add_item(book2)
library.add_item(magazine1)

print("Library Collection:")
for item in library.list_available_items():
    print(item)

library.borrow_item("1984")
library.borrow_item("The Great Gatsby")
library.borrow_item("The Great Gatsby")

print("\nBorrowed Items:")
for item in library.list_borrowed_items():
    print(item)

print("\nMost Borrowed Item:")
print(library.most_borrowed_item())
