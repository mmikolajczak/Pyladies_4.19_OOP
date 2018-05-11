class Book:  # klasa reprezentująca książkę w naszym programie
    def __init__(self, title, author, is_hardcovered, price, pages, quantity):
        self.title = title
        self.author = author
        self.is_hardcovered = is_hardcovered
        self.price = price
        self.pages = pages
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} by {self.author}, price: {self.price}, quantity: {self.quantity}'

    def is_available(self):  # metoda sprawdzająca czy można aktualnie kupić daną książke (czy stan magazynowy jest większy od zera)
        return self.quantity > 0


BOOKS_LIST = [  # lista słowników, zawierających dane o książkach na podstawie których stworzymy obiekty naszej powyższej klasy
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

    def __init__(self, books):  # inicjalizujemy księgarnie, listą obiektów typu Book
        self.books = books

    def __str__(self):  # reprezentacja tekstowa księgarni - wypisujemy po prostu w kolejnych liniach informacje o kolejnych
                        # książkach
        bookstore_str_representation = 'Bookstore current state:\n'  # zaczynamy tworzyć naszą reprezentacje tekstową od linii-nagłówka
        books_str_representations = []  # następnie inicjalizujemy pustą jistę, na reprezentacje stringowe poszczególnych książek
        for book in self.books:  # dla każdej książki
            books_str_representations.append(str(book))  # dodajemy jej reprezentacje do stworzonej w tym celu listy
        bookstore_str_representation += '\n'.join(books_str_representations)  # a następnie tworzymy z tej listy jeden łańcuch
                                                                              # znaków, w którym książki są rozdzielone nowa linią,
                                                                              # przy pomocy metody .join()
        return bookstore_str_representation  # zwracamy gotową reprezentację

    def _find_book(self, title, author):  # metoda pomocnicza, nieprzeznaczona do użytku poza klasą (ogólna konwencja nazewnicza
                                          # zakłada, żeby zaczynać nazwy takich metod "_"), która wyszukuje w posiadanych
                                          # książkach pozycje po parze tytuł/autor). jeśli dana książka nie znajduje się w
                                          # posiadanych zwracamy wartość pustą (None)
        for book in self.books:  # iteruj po wszystkich książkach
            if book.title == title and book.author == author:  # jeśli tytuł i autor aktualnej książki zgadza się z tym
                                                               # którego szukamy
                return book  # to znaczy, że znaleźliśmy szukaną pozycję i zwracamy ją
        return None  # jeśli nie znaleźliśmy pozycji w książkach to zwracamy wartość pustą (None)

    def is_available(self, title, author):  # metoda do sprawdzania czy książka jest dostępna
        found_book = self._find_book(title, author)  # najpierw wyszukujemy książkę po tytule i autorze
        return found_book is not None and found_book.is_available()  # zwaracamy czy znaleźliśmy daną pozycję w księgarni
                                                                     # i jeśli tak, to czy jest choć jedna w magazynie

    def make_promotion(self, multiplier):  # metoda do modyfikacji cen wszystkich książek o podany mnożnik
        for book in self.books:  # dla wszystkich książek w księgarni
            book.price *= multiplier  # zmień cenę na taką, by miała wartość równą wartości oryginalna_cena * mnożnik

    def sell_book(self, title, author):  # metoda do sprzedaży pojedynczej książki (o przakzanym tytule/autorze)
        book = self._find_book(title, author)  # próbujemy znaleźć książkę w rejestrze księgarni
        if book is not None and book.is_available():  # jeśli nam się udało i dodatkowo jest ona dostępna w magazynie
            book.quantity -= 1  # zmienjszamy liczebność książki w magazynie
            print(f'Sprzedanao ksiazke: {book}') # i "sprzedajemy ją" poprzez wypisanie komunikatu
        else:
            print('Nie sprzedano książki - brak w asortymencie')  # w innym przypadku wyświetlamy komunikat o niepowodzeniu sprzedaży

    # oczywiście księgarnia powinna mieć też pewnie jakieś inne metody (np. uzupełnianie stanu czy dodawanie nowej książki -
    # jeśli chcesz to nie krępuj się i spróbuj dodać je w ramach własnych ćwiczeń

    def __contains__(self, item):  # dodatek - wspominaliśmy sobie o metodach magicznych - otóż jest ich poza __init__ i
                                   # __str__ całkiem sporo. niektóe z nich odpowiadają między innymi za zachowanie się obiektu
                                   # w przypadku zastosowania na nim podstawowoych sybmoli czy słów kluczowych, przykładowo
                                   # __add__ odpowiada za zachowanie gdy spróbujemy "dodać" obiekt (poprzez "+"). contains
                                   # opdowiada za wynik zwrócony w przypadku użycia na obiekcie słowa "in". zwyczajowo
                                   # staramy się, żeby nasze implementacje tych metod realizowały zadania analogiczne jak przy
                                   # użyciu na obiektach wbudowanych (czyli in powinno sprawdzać czy jakiś obiekt znajduje się
                                   # w kolekcji/innym obiekcie - co też robimy w naszym przypadku, sprawdzając czy dana
                                   # para autor/tytuł znajduje się w księgarni)
        author, title = item  # rozpakowujemy przekazaną krotkę (tuple)
        return self._find_book(author, title) is not None  # i zwracamy czy księgarnia ma w rejestrze taką poyzcję


books = [Book(**book_info) for book_info in BOOKS_LIST]  # tworzymy listę książek (tutaj akurat używająć comprehension), z danych
                                                         # w naszej liście słowników (** rozpakowuje aktualny słownik i przekazuje jego
                                                         # wartości do funckji (w tym przypadku __init__), przykladowo:
                                                         # person_data_dict = {'name': 'Jan', 'surname': 'Kowalski'}
                                                         # person = Person(**person_data_dict)
book_store = BookStore(books)
print(book_store)  # możemy wyświetlić sobie stan księgarni w czytelnej formie - ponieważ zaimplementowaliśmy __str__)
book_store.sell_book('A Study in Scarlet', 'Arthur Conan Doyle')  # sprzedajemy książkę (co właściwie się nie powiedzie bo
                                                                  # nie ma jej w magazynie)
book_store.sell_book('Game of Thrones', 'George R. R. Martin')  # sprzedajemy książkę ( tym razem pomyślnie)
print(book_store)  # sprawdźmy, jak po sprzedażach zmienił się stan księgarni
book_store.make_promotion(3.0)  # fajna promocja, z okazji dnia chcwiego księgarza ^^
print(book_store)  # sprawdźmy, jak prezentują się ceny po naszej "promocji"
print(('Game of Thrones', 'George R. R. Martin') in book_store)  # możemy sprawdzić czy dana książka jest w księgarni przy
                                                                # pomocy in - ponieważ zaimplementowaliśmy contains
