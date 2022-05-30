def is_even(num):
    num = int(num)
    return num % 2 == 0


def main():
    numbers = input('Podaj listę liczb oddzielonych przecinkiem: ')
    numbers = numbers.split(',')
    for num in numbers:
        result = is_even(num)
        if result:
            print(num)


main()
