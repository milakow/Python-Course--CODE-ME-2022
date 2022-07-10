#Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.
class Animals:
    def __init__(self):
        print('I am an animal.')

class Mammal(Animals):
    def __init__(self):
        print('I\'m mammal. My first food is my mother\'s milk.')
        super().__init__()

class Human(Mammal):
    def __init__(self):
        print('Hi. I\'m human. :)')
        super().__init__()

h = Human()

print(Human.__mro__)