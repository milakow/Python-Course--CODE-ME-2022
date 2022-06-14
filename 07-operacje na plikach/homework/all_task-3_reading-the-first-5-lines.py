#3▹ Wyświetl tylko 5 pierwszych linii
def show_five_lines(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()
        print(*content[0:5])


def main():
    filename = input('Enter the name of the file: ')
    show_five_lines(filename)


main()
