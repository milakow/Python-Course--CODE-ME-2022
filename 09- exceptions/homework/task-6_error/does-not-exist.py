#Wywołaj błąd związany z otwarciem pliku. Spróbuj odczytać plik, który nie istnieje.Obsłuż w dowolny sposób każdy z powyższych błędów.
def get_name():
    return input('Enter the name of the file: ')

def main():
    filename = get_name()
    try:
        with open(filename, 'r') as f:
            text = f.read()
            print(text)
    except FileNotFoundError as e:
        print(f'Error \'{e}\' was found.')


if __name__ == '__main__':
    main()
