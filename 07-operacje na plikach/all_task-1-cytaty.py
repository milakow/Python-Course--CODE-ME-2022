# Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
#zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

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
    filename = input('Enter the name of file: ')
    quote = pick_quote(filename)
    show(quote)


main()
