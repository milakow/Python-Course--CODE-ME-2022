def circle_area(radius):
    pi = 3.14
    return pi * radius ** 2

user_radius = float(input('Podaj promień koła: '))
area = circle_area(user_radius)
print(f'Pole koła wynosi {area}')
