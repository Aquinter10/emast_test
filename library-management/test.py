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

from database import connect_db, create_tables

def add_book_to_db(title, type_):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (title, type, is_borrowed, borrow_count) VALUES (?, ?, ?, ?)",
        (title, type_, 0, 0)
    )
    conn.commit()
    conn.close()

def list_books_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return items

if __name__ == "__main__":
    create_tables()
    add_book_to_db("The Great Gatsby", "Book")
    add_book_to_db("1984", "Book")
    print("Books in database:")
    for item in list_books_from_db():
        print(item)