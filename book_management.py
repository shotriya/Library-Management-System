 
import json

class Book:
    def __init__(self, title, author, isbn, available=True):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = available

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}"

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

# Add other book types if needed (e.g., FictionBook, NonFictionBook, etc.)
# class FictionBook(Book):
#     pass

# class NonFictionBook(Book):
#     pass

class BookManager:
    def __init__(self, filename='books.json'):
        self._filename = filename
        self._books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self._filename, 'r') as f:
                data = json.load(f)
                self._books = [Book(**book) for book in data]
        except FileNotFoundError:
            pass

    def save_books(self):
        with open(self._filename, 'w') as f:
            json.dump([book.__dict__ for book in self._books], f, indent=4)

    def add_book(self, title, author, isbn):
        if any(book.isbn == isbn for book in self._books):
            raise ValueError("ISBN already exists in the library.")
        new_book = Book(title, author, isbn)
        self._books.append(new_book)
        self.save_books()

    def list_books(self):
        if not self._books:
            print("No books found in the library.")
        else:
            for book in self._books:
                print(book)

    def find_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
