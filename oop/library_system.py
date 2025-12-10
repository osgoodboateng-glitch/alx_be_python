class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
class Ebook(Book):
    def __init__(self, file_size: int):
        self.file_size = file_size
        super().__init__(title, author)
    def __str__(self):
        return f"{self.title} by {self.author} [EBook, {self.file_size}MB]"
class PrintBook(Book):
    def __init__(self, page_count: int):
        self.page_count = page_count
        super().__init__(title, author)
     def __str__(self):
        return f"{self.title} by {self.author} [PrintBook, {self.page_count} pages]"
class Library:
    def add_book(self):
        self.books = []
     def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)