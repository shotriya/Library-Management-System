 
class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self._book_manager = book_manager
        self._user_manager = user_manager

    def checkout_book(self, user_id, isbn):
        user = self._user_manager.find_user(user_id)
        if not user:
            raise ValueError("User not found.")

        book = self._book_manager.find_book(isbn)
        if not book:
            raise ValueError("Book not found.")

        if not book.available:
            raise ValueError("Book already borrowed.")

        book.available = False
        user.borrowed_books.append(book)
        self._book_manager.save_books()
