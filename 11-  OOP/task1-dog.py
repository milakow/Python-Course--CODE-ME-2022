#Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę. atrybuty: imię, kolor sierści, rasę, metody: szczekaj, machaj ogonem; Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog():
    def __init__(self, name, hair, breed):
        self.name = name
        self.hair = hair
        self.breed = breed

    def bark(self):
        print('woof! woof!')

    def whip_tail(self):
        print('I\'m a happy doggo')


atos = Dog('Atos', 'black and white', 'Alaskan malamute')
helena = Dog('Helena', 'vanilla', 'Labrador')


print(f'{atos.name} has {atos.hair}hair and is {atos.breed}')
helena.whip_tail()
atos.bark()
