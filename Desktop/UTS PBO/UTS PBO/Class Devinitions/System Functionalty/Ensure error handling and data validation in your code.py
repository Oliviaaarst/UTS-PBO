class Book:
    def __init__(self, book_id, title, author, shelf_location="", status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.shelf_location = shelf_location
        self.status = status

    def get_book_id(self):
        return self.book_id
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_shelf_location(self):
        return self.shelf_location
    def set_shelf_location(self, new_location):
        self.shelf_location = new_location
    def get_status(self):
        return self.status
    def set_status(self, new_status):
        self.status = new_status

class Librarian:
    def __init__(self, member_id, name, email): 
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        
    def get_member_id(self):
        return self.member_id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    
    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid book object provided.")
        if book.get_status() == "Borrowed":
            print("Book '{}' is already borrowed by another member.".format(book.get_title()))
            return
        self.borrowed_books.append(book)
        book.set_status("Borrowed")
        print("Book '{}' borrowed successfully by member {}.".format(book.get_title(), self.name))

    def return_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid book object provided.")
        if book not in self.borrowed_books:
            print("Book '{}' not borrowed by member {}.".format(book.get_title(), self.name))
            return
        self.borrowed_books.remove(book)
        book.set_status("Available")
        print("Book '{}' returned successfully by member {}.".format(book.get_title(), self.name))

if __name__ == "__main__":

    member1 = Librarian("M001", "Olivia Kristiani", "Oliviakristiani0@gmail.com")

    book1 = Book("B001", "Pemrograman Bahasa Phyton", "James")
    book2 = Book("B002", "Data Science Handbook", "Chealsea")

    try:
        member1.borrow_book(book1)
        member1.borrow_book(book2)
        member1.borrow_book("Invalid Book")
    except ValueError as e:
        print("Eror:", e)

    member1.return_book(book1)
    member1.return_book(book2)

    