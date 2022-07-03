#Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki. Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
#Utwórz kilka storczyków z różnymi parametrami.
class Orchid():
    kingdom= 'Plantae'

    def __init__(self, colour, flowering_time, type):
        self.colour = colour
        self.flowering_time = flowering_time
        self.type = type

    def get_water(self):
        print('I get water from the air.')

    def get_nutrients(self):
        print('I get nutrients from the dead part of host plant.')

falenopsis = Orchid('purple','by the end of autumn' ,'Phalaenopsis')
dendrobium = Orchid('multiple', 'since March till August', 'Dendrobium')
wanda = Orchid('blue', 'since spring till autumn', 'Vanda coerulea')

print(f'{falenopsis.type} is {falenopsis.colour}, blooms {falenopsis.flowering_time} and belongs to {falenopsis.kingdom}.')
print(f'Whereas {dendrobium.type} is {dendrobium.colour} and blooms {dendrobium.flowering_time}. {dendrobium.type} belongs to {dendrobium.kingdom} as well.')
wanda.get_water()
dendrobium.produce_nutrients()
