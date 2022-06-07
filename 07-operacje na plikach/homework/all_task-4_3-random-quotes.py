import random


def pick_quotes():
    with open(f'cytaty.txt', encoding= 'utf-8') as fopen:
        quotes = fopen.readlines()
        for choices in range(3):
            quote = random.choice(quotes)
            print(quote)


def main():
    pick_quotes()

main()