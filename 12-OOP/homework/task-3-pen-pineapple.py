#Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.
class Pen:
    def __init__(self, color):
        self.color = color
        print('I have a pen.')

class Pineapple:
    def __init__(self, size):
        self.size = size
        print('I have pineapple.')


class PenPineapple(Pen, Pineapple):
    def __init__(self, color, size):
        Pen.__init__(self, color)
        Pineapple.__init__(self, size)
        print('Pen, pineapple, apple, pen!')


john = PenPineapple('blue', 'medium')
print(f'John has {john.color} pen.')
