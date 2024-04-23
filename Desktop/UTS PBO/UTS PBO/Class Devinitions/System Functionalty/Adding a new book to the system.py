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
    
    def set_shelf_lacation(self, new_location):
        self.shelf_location = new_location

    def get_status(self):
        return self.status
    
    def set_status(self, new_status):
        self.status = new_status

def add_new_book(book_list, book_id, title, author, shelf_location="", status="Available"):
    new_book = Book (book_id, title, author, shelf_location, status)
    book_list.append(new_book)
    print("Book added succesfully!")

if __name__ == "__main__":

    book = []

    add_new_book(book, "B001", "Python Programing", "Olivia", "A3")

    print("\nBook List:")
    for book in book:
        print("Book ID:", book.get_book_id())
        print("Title:", book.get_title())
        print("Author:", book.get_author())
        print("Shelf Location:", book.get_shelf_location())
        print("Status:", book.get_status())
        print()
        