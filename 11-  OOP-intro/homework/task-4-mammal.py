#Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.
class Mammal():
    kingdom = 'Animalia'
    first_food = 'mother\'s milk'
    limb_num = 4

    def __init__(self, type, limbs, food, movement):
        self.type = type
        self.limbs = limbs
        self.food = food
        self.movement = movement

    def breathe(self):
        print(f'{self.type} breathes by lungs.')

    def eat(self):
        print(f'{self.type} eats {Mammal.first_food} when they are young and then {self.food}')

def main():
    bat = Mammal('bat', '2 wings', 'insects', 'flying')
    dolphin = Mammal('dolphin', '2 flippers', 'fish and squid', 'swimming')
    giraffe = Mammal('giraffe', '4 legs', 'leaves, fruits, and flowers', 'running')

    print(f'{bat.type} eats {bat.food} and moves by {bat.movement} with {bat.limbs}. {bat.type} belongs to {bat.kingdom}.')
    print(f'{giraffe.type} eats {giraffe.food} and moves by {giraffe.movement} with {giraffe.limbs}. Its first food is {giraffe.first_food} like all mammals. ')
    dolphin.eat()
    giraffe.breathe()
if __name__ == '__main__':
    main()
