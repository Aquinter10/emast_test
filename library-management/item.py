class Item:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True

    def return_item(self):
        self.__is_borrowed = False

    def is_borrowed(self):
        return self.__is_borrowed

    def get_details(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Book(Item):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.__isbn = isbn

    def get_details(self):
        return f"Book: {self._Item__title}, Author: {self._Item__author}, ISBN: {self.__isbn}"


class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_details(self):
        return f"Magazine: {self._Item__title}, Author: {self._Item__author}, Issue: {self.__issue_number}"