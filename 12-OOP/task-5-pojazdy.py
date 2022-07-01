#Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki. Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane. Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def feature(self):
        pass

    @abstractmethod
    def document(self):
        pass


class Bike(Vehicle):
    def feature(self):
        print('has two wheels')

    def document(self):
        print('bicycle card')

class Car(Vehicle):
    def feature(self):
        print('has four wheels and is smaller')

    def document(self):
        print('driving license- cat.B')

class Truck(Vehicle):
    def feature(self):
        print('has four wheels and is bigger')

    def document(self):
        print('driving license- cat. C+E')


def main():
    b = Bike()
    b.document()
    b.feature()

    c = Car()
    c.document()
    c.feature()

    t = Truck()
    t.document()
    t.feature()


if __name__ == '__main__':
    main()
