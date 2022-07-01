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

c = Cat()
print(Cat.__mro__)