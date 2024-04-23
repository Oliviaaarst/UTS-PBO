class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.shelf_location = ""  
        self.status = ""

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

# penggunaan pada contoh:

# membuat objek book
book1 = Book("B008", "Queen of tears", "Jiwon")

# Mendapatkan informasi buku
print("\nBook Information:")
print("ID:", book1.get_book_id())
print("Title:", book1.get_title())
print("Author:", book1.get_author())
print("Shelf Location:", book1.get_shelf_location())
print("Status:", book1.get_status())

# mengatur shelf location buku
book1.set_shelf_location("A3")
print("Update Shelf Location:", book1.get_shelf_location())

# mengatur status buku
book1.set_status("Available")
print("Update Status:", book1.get_status())