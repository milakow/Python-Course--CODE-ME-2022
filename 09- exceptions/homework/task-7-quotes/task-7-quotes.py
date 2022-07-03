#Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami. Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.
import random

def pick_quote(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()
        quote = random.choice(content)
        return quote

def show(quote):
    quote = quote.split("-")
    separator = '*' * 150
    print('\n Quote of the day is: \n')
    print(separator)
    print(quote[0].center(len(separator)))
    print(f'\n The author: {quote[1]}')
    print(separator)

def main():
    while True:
        try:
            filename = input('Enter the name of file: ')
            quote = pick_quote(filename)
            show(quote)
        except FileNotFoundError as er:
            print(f'Error \'{er}\' was found. Try to enter the name of the file one more time.')
        except AttributeError as er:
            print(f'Error \'{er}\' was found. Try to enter the name of the file one more time.')


if __name__ == '__main__':
    main()
