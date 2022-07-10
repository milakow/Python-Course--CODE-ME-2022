#Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
class Animals:
    def __init__(self):
        print('I am animal')

class Mammal(Animals):
    def __init__(self):
        super().__init__()
        print('milk')

class Cat(Mammal):
    def __init__(self):
        print('meow')
        super().__init__()

class Dog(Mammal):
    def __init__(self):
        print('woof, woof')
        super().__init__()

class Human(Mammal):
    def __init__(self):
        print('hi')
        super().__init__()

c = Cat()
print('--------')
d = Dog()
print('--------')
h = Human()

print(Cat.__mro__)