# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 11:32:03 2025

@author: willt
"""
import time


# phase 1: define author class


class Author:

    def __init__(self, name: str, nationality: str):
        """initialize author with a name and nationality"""
        self.name = name
        self.nationality = nationality

    def __str__(self):
        """returns a string of the author"""
        return f"{self.name}, {self.nationality}"

    def describe(self):
        print(f"Author: {self.name}\nNationality: {self.nationality}")

# phase 2: define book class


class Book:

    def __init__(self, title: str, author: Author, genre: str, available: bool
                 = True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.borrowed_time = None

    def borrow(self):
        if self.available:
            self.available = False
            from datetime import datetime
            self.borrowed_time = datetime.now()
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            from datetime import datetime
            borrow_duration = datetime.now() - self.borrowed_time if\
                self.borrowed_time else None
            self.borrowed_time = None
            return borrow_duration
        else:
            print("Book was not yet borrowed.")

    def __str__(self):
        return f"{self.title} by {self.author}"

# phase 3: define the patron class


class Patron:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrowed_books_add(self, book: Book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("Book isn't available")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            duration = book.return_book()
            self.borrowed_books.remove(book)
            print(f"Returned {book}. Borrowed for {duration}")
        else:
            print("This book was not borrowed by this patron.")

    def __str__(self):
        return f"Patron: {self.name}, Email: {self.email}"


# phase 4: Library

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book: Book):
        self.books.append(book)

    def register_patron(self, patron: Patron):
        self.patrons.append(patron)

    def list_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book} - {status}")

    def list_borrowed_books(self):
        for book in self.books:
            if not book.available:
                print(f"{book} is borrowed.")

# phase 5: generate library


author1 = Author("Alestair Reynolds", "United Kingdom")
author2 = Author("Margart Atwood", "Canada")
author3 = Author("Yevgeny Zamyatin", "Russia")
author4 = Author("Harlan Ellison", "America")
book1 = Book("Pushing Ice", author1, "Science Fiction")
book2 = Book("I Have No Mouth, and I Must Scream", author4, "Science Fiction")
book3 = Book("We (novel)", author3, "Science Fiction")
book4 = Book("Oryx and Crake", author2, "Science Fiction")
patron1 = Patron("Will", "will@exampleemailaddress.com")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.register_patron(patron1)

# phase 6: borrow and return books

patron1.borrowed_books_add(book1)
print(f"\033[31;47mThank you for using the public library self-checkout. Enjoy\
 reading {book1}!\n\n\033[0m")
time.sleep(4)
patron1.return_book(book1)
print("\033[31;47mWelcome back to the public library self-checkout, let's get\
 you started.\033[0m")
library.list_books()
print(f"\033[31;47mThank you for using the public library self-checkout. Enjoy\
 reading {book2} & {book3}!\n\n\033[0m")
