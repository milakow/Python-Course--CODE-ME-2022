#Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.
class Shop:
    def __init__(self, cloth, size, price, colour):
        self.cloth = cloth
        self.size = size
        self.price = price
        self.colour = colour

    def watch(self):
        print(f'I like that {self.colour} {self.cloth}.')

    def try_on(self):
        print(f'{self.cloth} in size {self.size} fits perfectly.')

    def buy(self):
        print(f'I want to buy {self.cloth} which costs {self.price} EUR.')

    def retrn(self):
        print(f'I made a mistake when I bought {self.cloth}.')

shoes = Shop('shoes', '38.5', 40, 'white')
shoes.watch()
shoes.try_on()
shoes.buy()