#Wywołaj błąd związany z otwarciem pliku. Spróbuj odczytać wartość z pliku otwartym w trybie w. Obsłuż w dowolny sposób każdy z powyższych błędów.
def get_name():
    return input('Enter the name of the file: ')

def main():
    filename = get_name()
    try:
        with open(filename, 'w') as f:
            text = f.readlines()
            print(text)
    except IOError as e:
        print(f'Error \'{e}\' was found.')


if __name__ == '__main__':
    main()
