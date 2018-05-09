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