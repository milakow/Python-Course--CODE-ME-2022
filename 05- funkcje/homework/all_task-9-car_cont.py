def is_25_yo(year, brand):
    if 2022 - year >= 25:
        print(f'Gratulacje! Twój samochód {brand} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {brand} jest jeszcze zbyt młody.')


def is_original(appraiser_opinion):
    if appraiser_opinion >= 75:
        return True
    else:
        return False


def main():
    car = {'brand': 'rolls-royce', 'model': 'shadow II', 'year': 1965}
    car.update({'is_original': True})
    print(car)
    if is_25_yo(car['year'], car['brand']):
        print(is_25_yo(car['year'], car['brand']))
    appraiser_opinion = 60
    if is_original(appraiser_opinion):
        print(f'Gratulacje! Rzeczoznawca ocenił Twój samochód jako oryginalny.')
    else:
        print(f'Niestety twój samochód nie został zakwalifikowany jako oryginalny.')

main()
