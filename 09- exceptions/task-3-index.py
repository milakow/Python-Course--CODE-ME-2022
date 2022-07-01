#Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.
def get_user_choice(my_list: object, index: object) -> object:
    return round(1 / my_list[index], 4)


def main():
    my_list = [0, 90, 'si', True, None, 23.45, (1, 'a'), False, {}, [2, 2]]
    index = int(input('Pick a number index from the list, which will be divided: '))

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
