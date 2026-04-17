class Item:
    def __init__(self, item_id, title):
        self._item_id = item_id
        self._title = title

    def get_id(self):
        return self._item_id

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def display_info(self):
        print(f"ID: {self._item_id}, Title: {self._title}")
