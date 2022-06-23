#Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.
class Shop:
    def __init__(self, product=[]):
        self.cloth = product

    def watch(self):
        #for clothes in
        print('Niiice!')

    def try_on(self):
        print(f'{self.cloth} fits perfectly')

    def buy(self):
        print(f'{self.cloth} costs...')

    def retrn(self):
        print(f'I made a mistake when I bought this {self.cloth}.')

def main():
    clothes = Shop(['thirt', 'trousers', 'socks'])
    clothes.watch()
    clothes.try_on()
    clothes.buy()
    clothes.retrn()


if __name__ == '__main__':
    main()
