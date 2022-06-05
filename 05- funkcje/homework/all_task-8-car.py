def is_25_yo(year, brand):
    if 2022 - year >= 25:
        print(f'Gratulacje! Twój samochód {brand} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {brand} jest jeszcze zbyt młody.')


def main():
    car = {'brand': 'peugeot', 'model': '308', 'year': 2014}
    print(car)
    if is_25_yo(car['year'], car['brand']):
        print(is_25_yo(car['year'], car['brand']))


main()
