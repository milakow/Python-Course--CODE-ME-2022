#Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery
def upper_case(param):
    def upper_nested():
        result = param()
        return result.upper()
    return upper_nested

@upper_case
def get_text():
    return 'python'

def main():
    effect = get_text()
    print(effect)
    # print(get_text)


if __name__ == '__main__':
    main()
