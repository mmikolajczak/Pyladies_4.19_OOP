from abc import ABCMeta, abstractmethod


class Engine:

    def __init__(self, fuel_type, fuel_units_per_100_km):
        self.fuel_type = fuel_type
        self.fuel_units_per_100_km = fuel_units_per_100_km

    def get_required_fuel(self, nb_kilometres):
        return (nb_kilometres / 100) * self.fuel_units_per_100_km

    def work(self, fuel):
        if fuel[0] != self.fuel_type:
            raise RuntimeError(f'Komunikat silnika: podano zły rodzaj paliwa {fuel[0]}.'
                               f' Wlej mi {self.fuel_type} a nie jakiś olej z Biedronki.')
        print('Pyr pyr pyr, brum, brum.')
        return (fuel[1] / self.fuel_units_per_100_km) * 100


class FuelSource(metaclass=ABCMeta):

    @abstractmethod
    def get_fuel(self, units):
        pass

    def refill(self, units):
        pass


class GasFuelSource(FuelSource):

    def __init__(self, initial_units):
        self._units = initial_units

    def get_fuel(self, units):
        if units < self._units:
            self._units -= units
            return ('gas', units)
        else:
            return ('gas', self._units)

    def refill(self, units):
        self._units += units


class RoadCounter:

    def report_traveled_distance(self, distance):  # właściwie może to być metoda klasy, bez użycia self
        print(f'Traveled {distance} km.')


class MilesRoadCounter(RoadCounter):

    def report_traveled_distance(self, distance):
        distance_in_miles = distance / 1.61
        print(f'Traveled {round(distance_in_miles, 2)} miles.')


class Car:

    def __init__(self, engine, fuel_source, road_counter, color):
        self._engine = engine
        self._fuel_source = fuel_source
        self._road_counter = road_counter
        self.color = color

    def ride(self, nb_kilometers):
        units_required = self._engine.get_required_fuel(nb_kilometers)
        fuel = self._fuel_source.get_fuel(units_required)
        kilometers_traveled = self._engine.work(fuel)
        self._road_counter.report_traveled_distance(kilometers_traveled)


old_engine = Engine('gas', 20)
gas_source = GasFuelSource(50)
trabancik = Car(old_engine, gas_source, RoadCounter(), 'red')


trabancik.ride(100)
trabancik.ride(100)
trabancik.ride(1000)


params = {'engine': Engine('gas', 5),
          'fuel_source': GasFuelSource(200),
          'road_counter': MilesRoadCounter(),
          'color': 'green'}
super_trabancik = Car(**params)

super_trabancik.ride(1000)
