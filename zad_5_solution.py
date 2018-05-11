class Book:
    def __init__(self, title, author, is_hardcovered, price, pages, quantity):
        self.title = title
        self.author = author
        self.is_hardcovered = is_hardcovered
        self.price = price
        self.pages = pages
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} by {self.author}, price: {self.price}, quantity: {self.quantity}'

    def is_available(self):
        return self.quantity > 0


BOOKS_LIST = [
    {
        'title': 'Harry Potter and the Chamber of Secrets',
        'author': 'J. K. Rowling',
        'is_hardcovered': False,
        'price': 15.70,
        'pages': 358,
        'quantity': 23,
    },
    {
        'title': 'Lord of the Rings: The Two Towers',
        'author': 'J. R. R. Tolkien',
        'is_hardcovered': False,
        'price': 21.30,
        'pages': 488,
        'quantity': 7,
    },
    {
        'title': 'Game of Thrones',
        'author': 'George R. R. Martin',
        'is_hardcovered': True,
        'price': 24.99,
        'pages': 712,
        'quantity': 55,
    },
    {
        'title': 'A Study in Scarlet',
        'author': 'Arthur Conan Doyle',
        'is_hardcovered': True,
        'price': 21.37,
        'pages': 234,
        'quantity': 0,
    },
]


class BookStore:

    def __init__(self, books):
        self.books = books

    def __str__(self):
        return 'Bookstore current state:\n' + '\n'.join([str(book) for book in self.books])

    def __contains__(self, item):
        author, title = item
        return self._find_book(author, title) is not None

    def _find_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                return book
        return None

    def is_available(self, title, author):
        found_book = self._find_book(title, author)
        return found_book is not None and found_book.is_available()

    def make_promotion(self, multiplier):
        for book in self.books:
            book.price *= multiplier

    def sell_book(self, title, author):
        book = self._find_book(title, author)
        if book.is_available():
            book.quantity -= 1
            print(f'Sprzedanao ksiazke: {book}')
        else:
            print('Nie sprzedano książki - brak w asortymencie')


books = [Book(**book_info) for book_info in BOOKS_LIST]
book_store = BookStore(books)
print(book_store)
book_store.sell_book('A Study in Scarlet', 'Arthur Conan Doyle')
book_store.sell_book('Game of Thrones', 'George R. R. Martin')
print(book_store)
book_store.make_promotion(3.0)
print(book_store)
print(('Game of Thrones', 'George R. R. Martin') in book_store)
