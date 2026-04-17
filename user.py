class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._borrowed_books = []

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def display_info(self):
        print(f"User ID: {self._user_id}, Name: {self._name}, Borrowed: {len(self._borrowed_books)}")
