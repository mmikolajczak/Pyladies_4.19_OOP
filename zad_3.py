"""
W pliku email_sender, znajduje się klasa odpowiadająca za wysyłanie wiadomości email z konta gmail.
Jest ona klasą abstrakcyjną , którą należy odpowiednio nadpisać/zaimplementować metody w klasach dziedziczących.
Przeanalizuj ją, a następnie stwórz podklasę BirthdayWishesSender, która korzystając z obiektu Person
będzie generować życzenia urodzinowe w następującym formacie:

Drog[a lub i] imię,
spóźnione wszystkiego najlepszego z okazji twoich age urodzin.

i wysyłać je na podany adres email.
(w przypadku problemów przy wysyłaniu -> patrz slajdy)

Wskazówka, jak rozróżnić imię żeńskie od męskiego:
Cytat:
"Otóż wszystkie żeńskie imiona w języku polskim kończą się na literę a.
Natomiast wszystkie męskie imiona kończą się na wszystkie inne litery, tylko nie a.
Są drobne wyjątki tj. istnieje kilka męskich imion, które kończą się na a: (Kuba, Kosma, Dyzma, Barnaba i Bonawentura).
Wszystkie te imiona z wyjątkiem Kuby można pominąć, gdyż nie są zbyt popularne."
Źródłem tego cytatu jest Internet, więc to musi być prawda ;) (a przynajmniej tak przyjmijmy)
"""