"""
Szybka rozgrzewka: stwórz klasę Person, posiadającą następujące atrybuty: imię, nazwisko
i data urodzenia.
Dodatkowo, klasa powinna posiadać metodę age, która zwróci aktualny wiek osoby,
wyliczany na podstawie jej roku urodzenia i aktualnej daty.
Wskazówka: zaimportuj i wykorzystaj wbudowany moduł datetime, który posiada w sobię klasę do obsługi dat.
Dokumnetacja: https://docs.python.org/3/library/datetime.html#datetime.date
Postaraj się również, aby po użycie funkcji print na obiekcie klasy osoba,
skutkowało wypisaniem łanucha znaków w formacie: nazwisko imie, lat: wiek
Przykład:
>>> iron_man = Person('Anthony', 'Stark', datetime.date(1970, 5, 29))
>>> print(iron_man)
output: Stark Anthony, lat: 47
Następnie stwórz 3 różne obiekty klasy osoba i wypisz informacje o nich na ekranie.
"""

import datetime  # importujemy moduł datetime, który przyda się do obsługi dat (jest to wbudowany moduł Pythona)


class Person:  # deklaracja klasy Person (słowo kluczowe class + nazwa klasy, ogólna konwencja nazewnicza = każdy człon
               # w nazwie klasy zaczynamy z dużej litery, reszta nazwy pisana małymi literami np. ShipBuilder)

    def __init__(self, name, surname, birthdate):  # metoda inicjalizująca, która jest wywoływana w momencie tworzenia obiektu
                                                   # klasy (np. podczas wywołania Person('Jan', 'Kowalski', data). Pierwszym,
                                                   # "domyślnym" parametrem jest self (nie tylko w tej, a każdej metodzie),
                                                   # (metoda = funkcja, tylko w kontekście klasy), czyli konketny obiekt klasy.
                                                   # metody, które zaczynają i kończą się na __są tzw "magicznymi" metodami,
                                                   # mającymi jakiąś specjalną rolę (np. nasz init - który jest wykonywany gdy tworzymy obiekt)
        self.name = name
        self.surname = surname
        self.birthdate = birthdate  # tworzymy nowe atrybuty w naszym obiekcie - i przypisujemy do nich argumeny __init__

    def age(self):  # metoda (trzeba więc ją wywołać analogicznie do funkcji, tylko że na obiekcie), obliczająca wiek
                    # osoby na podstawie jej daty urodzin
        today = datetime.date.today()  # pobieramy aktualny dzień
        age = today.year - self.birthdate.year  # obliczamy różnicę między rokiem bieżącym a rokiem urodzenia osoby
        if today.month < self.birthdate.month and today.day < self.birthdate.day:  # z tym, że jeśli osoba nie miałą jeszcze
                                                                                   #  urodzin  w roku bieżącym...
            age -= 1  # ...to musimy zmniejszyć tą różnicę o jeden
        return age  # zwracamy wynik

    def __str__(self):  # specjalna ("magiczna") metoda, odpowiadająca za konwersję obiektu na łańcuch znaków (string),
                        # np. przy przekazaniu obiektu do funkcji print
        return f'{self.surname} {self.name}, lat: {self.age()}'  # tzw. f-string, który w miejscach pomiędzy nawiasami {}
                                                                 # umieści stringową reprezentacje wpisanych tam zmiennych


iron_man = Person('Anthony', 'Stark', datetime.date(1970, 5, 29))  # tworzymy 3 obiekty naszej klasy Person
print(iron_man)
captain_america = Person('Steve', 'Rogers', datetime.date(1918, 7, 4))
doctor_strange = Person('Stephen', 'Strange', datetime.date(1930, 11, 1))

for person in (iron_man, captain_america, doctor_strange):  # iterujemy bo naszych stworzonych obiektach
                                                            # (warto zwrócić uwagę jak to robimy, jak widać, nie musimy
                                                            # najpierw specjalnie tworzyć do tego listy naszzych obiektów
                                                            # a zrobić to w przedstawiony sposób)
    print(person)  # wypisujemy osobę (zadziała metoda __str__, i dostaniemy wynik zgodny z tym jak zdefiniowaliśmy zwracany
                   # przez nią string)
