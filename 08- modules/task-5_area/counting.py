#Stwórz moduł obliczający pola różnych figur. W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku.
from area import count_circle_area, count_square_area, count_rectangle_area


def main():
    rooms = {
        'square': [2, 2, 4],
        'circle': [2, 3, 4],
        'rectangle': [[2, 3], [4, 5]]

    }
    total_area = 0

    for shape, rooms in rooms.items():
        if shape == 'square':
            for room in rooms:
                total_area += count_square_area(room)
        elif shape == 'circle':
            for room in rooms:
                total_area += count_circle_area(room)
        elif shape == 'rectangle':
            for room in rooms:
                a, b = room
                total_area += count_rectangle_area(a, b)
        else:
            print('I don\'t recognize this shape.')

    print(f'The total area is {total_area}m2.')


if __name__ == '__main__':
    main()