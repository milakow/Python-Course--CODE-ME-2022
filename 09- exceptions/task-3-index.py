def get_user_choice(my_list: object, index: object) -> object:
    result = 1 / my_list[index]


def main():
    my_list = [0, 90, 'si', True, None, 23.45, (1, 'a'), False, {}, [2, 2]]
    index = int(input('Podaj indeks liczby z list, która zostanie poddana operacji dzielenia: '))

    try:
        effect = get_user_choice(my_list, index)
        print(effect)
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    except IndexError:
        print('You picked incorrect id')
    except ZeroDivisionError:
        print('It is impossible to divide by 0.')
    finally:
        print('Done')


if __name__ == '__main__':
    main()
