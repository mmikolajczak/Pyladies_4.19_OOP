import math


class Shape:  # klasa kształt, będąca szkieletem określającym jakie zachowania/metody powinny mieć dziedziczące kształty
              # jej funkcje nie mają natomias implementacji (bo jak w sumie obliczyć pole/obwód nieokreślonego kształtu)
              # (w zasadzie nie powinniśmy mieć nawet możliwości stworzenia takiej klasy - więcej o takiej sytuacji znajdziesz
              # na slajdach (hasło: klasa abstrakcyjna))

    def area(self):
        raise NotImplemented()  # nie mamy tu żadnej implementacji i nie powinniśmy obliczać pola/obwodu kształtu - co sygnalizujemy wyjątkiem

    def perimeter(self):
        raise NotImplemented()


class Rectangle(Shape):  # dziedziczymy po kształcie

    def __init__(self, side_a, side_b):  # o prostokącie wiemy już więcej niż o kształcie, i wiemy jakie atrybuty powinien on
                                         # mieć (konkretnie dwa boki) i odpowiednio go inicjalizujemy
        self.side_a = side_a
        self.side_b = side_b

    def area(self):  # implementujemy odpowiednio metody obliczające pole i obwód (natomiast nazwy metod i sposób wywołania
                     # pozostaje taki sam
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * self.side_a + 2 * self.side_b


class Square(Rectangle):  # kolejne dziedzicznie, tym razem z klasy rectangle - mimo, że ona sama też już z czegoś dziedziczy
                          # - nie ma w tym żadnego problemu i jest to jak najbardziej dozwolone

    def __init__(self, side):
        Rectangle.__init__(self, side, side)  # wywołujemy metodę __init__ klasy nadrzędnej (można użyć super), i przekazujemy
                                              # odpowiednio arguemnty -> otrzymaną długość boku kwadratu jako długość boków
                                              # a i b prostokąta. co jeszcze istotniejsze, nie musimy napisywać metod area
                                              # i perimeter - zostaną wtedy wykorzystane te odziedziczone po klasie nadrzędnej
                                              # (a dzięki temu jak wywołujemy __init__ prostokąta zadziałają one w zupełności
                                              # poprawnie


class Circle(Shape):  # Kolejna klasa będąca pochodną kształtu, wraz z odpowiednio przeciążonymi metodami
                      # (wykorzystujemy w nich stałą pi z zaimportowanego modułu wbudowanego math)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


def calculate_total_area(shapes):  # Funckja do obliczania całkowitej powierzchni przekazanej listy kształtów
                                   # zwróć uwagę na to, że każdy kształt musi mieć metodę area o dokładnie takich samych
                                   # parametrach - co pozwala na zliczanie pola w pętli poprzez po prostu wywołanie odpowiedniej
                                   # metody, nie zwracając w ogóle uwagi na to, jakiej klasy konkretnie jest obecny kształt.
    total_area = 0
    for shape in shapes:
        total_area += shape.area()  # dla każdego kształtu wywołujemy tą samą metodę, "interfejs" jest więc identyczny,
                                    # natomiast w jaki spobób obliczane jest faktyczne pole zależy od jej implementacji w
                                    # konkretnej klasie
    return total_area


# alternatywny sposób - przy wykorzystaniu wbudowanego sum i generator expresion (ciekawscy mogą wyszukać hasło
# comprehensions, niestety opis zagadnienienia trochę za dużo by tu zajął)
#def calculate_total_area(shapes):
#    return sum(shape.area() for shape in shapes)


# uwaga - kod poniżej prezentuje parę nowych, ciekawych możliwości - ale może być średnio zrozumiały
# prostsza wersja rozwiązanie znajduje się pod nim (wystarczy ją odkomentować, a tą zakomentować)

# welcome to world of little mindfuck - klasy w Pythonie same w sobie też są obiektami - możemy je więc śmiało przechowywać
# w listach czy słownikach albo przekazać do funkcji...
shapes_dict = {'circle': Circle,  # ...co robimy na przykład tutaj - deklarujemy słownik, w którym pod stringiem
                                  # z nazwą klasy jest przechowywana sama klasa
               'rectangle': Rectangle,
               'square': Square}

with open('do_pomalowania.txt', 'r') as f:  # klauzula with zastosowana w kontekście otwierania pliku gwarantuje, że zostanie
                                            # on automatycznie zamknięty
    shapes = []  # inicjalizujemy pustą listę kształtów
    for line in f:  # iterujemy po każdej linii w pliku
        values = line.split(' ')  # tworzymy listę wartości, rozdzielając linię na wartości według spacji (taka jeststruktura pliku)
        shape_type = values[0]  # pierwszą wartością jest string z nazwą klasy
        shape_params = [float(val) for val in values[1:]]  # z pozostałych wartości w linii tworzymy listę wartości float (comprehension)
        shapes.append(shapes_dict[shape_type](*shape_params))  # dodajemy do listy shapes: wybierając ze słownika wartość pod shape_type
                                                               # (czyli jakąś klasę), którą następnie tworzymy, przekazując jako argumenty
                                                               # wartości z shape_params

# uwaga: powyżej jest całkiem sporo nowych konceptów, natomiast można to rozwiązać bardziej tradycyjnie, z wykorzystaniem
# paru warunków
# with open('do_pomalowania.txt', 'r') as f:
#    shapes = []
#    for line in f:
#        values = line.split(' ')
#        if values[0] == 'circle':
#            shape = Circle(float(values[1]))
#        elif values[0] == 'rectangle':
#            shape = Rectangle(float(values[1]), float(values[2]))
#        elif values[0] == 'square':
#            shape = Square(float(values[1]))
#    shapes.append(shape)

total_area = calculate_total_area(shapes)  # wywołujemy wcześnie zdefiniowaną funkcję do obliczania pola listy kształtów
print(f'Łączna powierzchnia do pomalowania: {total_area}')  # o=i wyświetlamy sobie wynik
