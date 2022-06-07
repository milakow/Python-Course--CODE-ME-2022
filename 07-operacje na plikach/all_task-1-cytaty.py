import random


def pick_quote(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()

    quote = random.choice(content)
    return quote


def show(quote):
    quote = quote.split("-")
    print(quote)
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
