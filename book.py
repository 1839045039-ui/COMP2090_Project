from item import Item

class Book(Item):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self._author = author
        self._is_borrowed = False

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def is_borrowed(self):
        return self._is_borrowed

    def set_borrowed(self, status):
        self._is_borrowed = status

    def display_info(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        print(f"ID: {self._item_id}, Title: {self._title}, Author: {self._author}, Status: {status}")
