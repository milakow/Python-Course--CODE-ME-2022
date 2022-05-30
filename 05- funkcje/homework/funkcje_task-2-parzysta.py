def is_even(num):
    return num % 2 == 0


def main():
    number = int(input('Podaj liczbę: '))
    result = is_even(number)
    if result != True:
        print(f'Podana liczba {number} nie jest parzysta.')
    else:
        print(f'Podana liczba {number} jest parzysta')


main()

