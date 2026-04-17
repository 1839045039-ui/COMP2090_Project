class LibrarySystem:
    def __init__(self):
        self._books = []
        self._users = []

    def add_book(self, book):
        self._books.append(book)

    def add_user(self, user):
        self._users.append(user)

    def find_book_by_id(self, item_id):
        for book in self._books:
            if book.get_id() == item_id:
                return book
        return None

    def find_user_by_id(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                return user
        return None

    def show_all_books(self):
        for book in self._books:
            book.display_info()

    def search_book(self, keyword):
        found = False
        for book in self._books:
            if keyword.lower() in book.get_title().lower():
                book.display_info()
                found = True
        if not found:
            print("No matching book found")

    def borrow_book(self, user_id, item_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(item_id)

        if user is None or book is None:
            print("Invalid user or book")
            return

        if book.is_borrowed():
            print("Book is already borrowed")
            return

        book.set_borrowed(True)
        user.borrow_book(book)
        print("Borrow successful")

    def return_book(self, user_id, item_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(item_id)

        if user is None or book is None:
            print("Invalid user or book")
            return

        if not book.is_borrowed():
            print("Book is not borrowed")
            return

        book.set_borrowed(False)
        user.return_book(book)
        print("Return successful")
