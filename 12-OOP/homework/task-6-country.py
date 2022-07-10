#Utworz klasę Kraj, która zawiera informację o powierzchni. ludności, jaki język jest urzędowy, jakie miasto jest stolicą. Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy na liście krajów.
from abc import ABC, abstractmethod

class Country:
    def __init__(self, area, population, language, capital):
        self.area = area
        self.population = population
        self.language = language
        self.capital = capital

def main():
    portugal = Country(99.2, 10.3, 'portuguese', 'lisbon')
    spain = Country(505.99, 47.35, 'spanish', 'madrid')
    france = Country(543.94, 67.39, 'french', 'paris')
    print(type(portugal))
    countries = [portugal, spain, france]
    print(countries)


if __name__ == '__main__':
    main()

