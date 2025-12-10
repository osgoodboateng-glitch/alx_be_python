# Base class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


# Derived class: EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)   # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} [EBook, {self.file_size}MB]"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)   # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} [PrintBook, {self.page_count} pages]"


# Composition: Library
class Library:
    def __init__(self):
        self.books = []   # List to store Book, EBook, PrintBook instances

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
