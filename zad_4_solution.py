from abc import ABCMeta, abstractmethod  # importujemy z wbudowanego modułu abc elementy wymagane do tworzenia klas i metod abstrakcyjnych


class Engine:  # tworzymy klasę reprezentującą silnik

    def __init__(self, fuel_type, fuel_units_per_100_km):  # inicjalizator obiektu klasy Engine - jej atrybuty to typ paliwa
                                                           # i ile silnik spala go na 100km
        self.fuel_type = fuel_type
        self.fuel_units_per_100_km = fuel_units_per_100_km

    def get_required_fuel(self, nb_kilometres):  # metoda zwracająca ilość paliwa potrzebną do przejechania podanej w
                                                 # argumencie liczby kilometró
        return (nb_kilometres / 100) * self.fuel_units_per_100_km

    def work(self, fuel):  # metoda symulująca pracę silnika (wymagane do niej jest przekazanie pewnej ilości paliwa)
        if fuel[0] != self.fuel_type:  # sprawdzamy czy podany typ paliwa jest poprawny (przekazywane paliwo to tuple(typ, ilosc_jednostek)
            raise RuntimeError(f'Komunikat silnika: podano zły rodzaj paliwa {fuel[0]}.'
                               f' Wlej mi {self.fuel_type} a nie jakiś olej z Biedronki.')
        print('Pyr pyr pyr, brum, brum.')  # silnik bardzo intensywnie pracuje ^^
        return (fuel[1] / self.fuel_units_per_100_km) * 100  # i zwraca liczbę przejechanych na przekazanym paliwie kilometrów


class FuelSource(metaclass=ABCMeta):  # abstrakcyjna klasa reprezentująca źródło paliwa. zawiera sygnatury metod, które klasy pochodne
                                      # powinny implementować - metodę służącą do pobierania paliwa ze zbiornika i jego uzupełniania

    @abstractmethod
    def get_fuel(self, units):
        pass

    @abstractmethod
    def refill(self, units):
        pass


class GasFuelSource(FuelSource):  # tworzymy klasę reprezentującą już konkretne źródło paliwa (benzyny), i implementującą metody
                                  # które takie źródło powinno posiadać

    def __init__(self, initial_units):  # inicjalizujemy obiekt (ma on pewną początkową ilość benzyny po stworzeniu)
                                        # (poprzez nazwanie zmiennych/metod z początkiem "_" wskazujemy, że mnie powinny być
                                        # one wykorzystywane/modyfikowane poza metodami danego obiektu, jest to jedna z
                                        # przyjętych konwencji nazewniczych)
        self._units = initial_units

    def get_fuel(self, units):  # metoda pobierająca paliwo ze źródła
        if units <= self._units:  # jeśli posiadamy wystarczającą ilość paliwa
            self._units -= units
            return ('gas', units)  # to zmniejszamy stan szbiornika o żądaną wartośc i zwracamy paę (typ_paliwa, ilość_żądanych_jednostek)
        else:
            self._units = 0
            return ('gas', self._units)  # gdy paliwa jest mniej niż było żądane - zwracamy tyle ile mamy, również w postaci
                                         # pary (typ_paliwa, ilość_posiadancyh_jednostek) a stan zbiornika zerujemy

    def refill(self, units):  # upraszczamy przypadek, po prostu zakładamy że wlaliśmy ileś jednostek paliwa
                              # więcej a zbiornik jest nieograniczony
        self._units += units


class RoadCounter:  # prosta klasa z jedną metodą - służącą do wypisywania na ekranie raportu o przejechanym dystanie
                    # implementuje ona domyślny sposób raportowania - w kilometrach

    def report_traveled_distance(self, distance):
        print(f'Traveled {distance} km.')


class MilesRoadCounter(RoadCounter):  # nasza klasa do raportowania (dziedziczymy z RoadCounter, ale właściwie moglibyśmy
                                      # to ominąć, nie korzystamy ż niczego co ona zapewnia/posiada, natomiast musimy zapewnić
                                      # zgodność interfejsu (czyli sygnatury metod)). klasa raportuje przebyty dystans w milach.

    def report_traveled_distance(self, distance):
        distance_in_miles = distance / 1.61
        print(f'Traveled {round(distance_in_miles, 2)} miles.')


class Car:  # klasa symulująca samochód

    def __init__(self, engine, fuel_source, road_counter, color):  # inicjalizacja - mamy tu do czynienia z obiektem który jest
                                                                   # kompozycją - zawiera w sobie inne obiekty (warto zauważyć,
                                                                   # że nie wyklucza to oczywiście jednoczesnego posiadania zmiennych
                                                                   # z typami wbudowanymi (np. string określający kolor naszego
                                                                   # samochodu)
        self._engine = engine
        self._fuel_source = fuel_source
        self._road_counter = road_counter
        self.color = color

    def ride(self, nb_kilometers):  # metoda rozkazująca samochodowi przejechać określoną liczbę kilometrów
                                    # warto zwrócić dużą uwagę na to, jak wygląda współpraca zawierancyh w samochodzie obiektów,
                                    # i to jak modyfikują i korzystają one ze swojego stanu.
        units_required = self._engine.get_required_fuel(nb_kilometers)  # najpierw zwracamy się do obiektu silnika o to, ile
                                                                        # jednostek jest mu potrzebne na przejechanie żądanego
                                                                        # dystansu
        fuel = self._fuel_source.get_fuel(units_required)  # następnie prosimy o taką ilość paliwa nasze źródło
        kilometers_traveled = self._engine.work(fuel)  # podajemy uzyskaną ilość paliwa do silnika, który wykorzystuje je
                                                       # do wykonania pracy, a następnie zwraca ile kilometrów udało się
                                                       # przejechać wykorzystując przekazane paliwo
        self._road_counter.report_traveled_distance(kilometers_traveled)  # ilość kilometrów zwrócona przez silnik jest następnie
                                                                          # podana naszemu obiektowi, odpowiedzialnmu za raprotwanie,
                                                                          # które on odpowiednio wykonuje


old_engine = Engine('gas', 20)
gas_source = GasFuelSource(50)
trabancik = Car(old_engine, gas_source, RoadCounter(), 'red')  # tworzymy nowy samochód, składając go z obiektów różnych klas


trabancik.ride(100)
trabancik.ride(100)
trabancik.ride(1000)  # i testujemy trochę jego działanie


params = {'engine': Engine('gas', 5),
          'fuel_source': GasFuelSource(200),
          'road_counter': MilesRoadCounter(),
          'color': 'green'}
super_trabancik = Car(**params)  # tworzymy nowy, lepszy samochód, z lepszymi osiągami i wykorzystujący naszą nową klasę
                                 # do raportowania przebytego dystansu w milach
                                 # warto zwrócić uwagę, w jaki sposób przekazujemy paramtery ze słownika

super_trabancik.ride(1000)
