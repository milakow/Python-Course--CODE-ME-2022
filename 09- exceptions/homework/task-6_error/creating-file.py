#Wywołaj błąd związany z otwarciem pliku. Spróbuj utworzyć plik, który już istnieje w trybie x. Obsłuż w dowolny sposób każdy z powyższych błędów.
def get_name():
    return input('Enter the name of the file: ')

def main():
    filename = get_name()
    try:
        with open(filename, 'x') as f:
            text = f.readlines()
            print(text)
    except FileExistsError as e:
        print(f'Error \'{e}\' was found.')


if __name__ == '__main__':
    main()
