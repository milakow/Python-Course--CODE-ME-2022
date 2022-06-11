`from area import count_circle_area, count_square_area


def main():
    shape = 'square'
    if shape == 'square':
        length_a = int(input('Enter the length of the edge: '))
        print(count_square_area(length_a))
    elif shape == 'circle':
        radius = int(input('Enter the radius of the circle: '))
        print(count_circle_area(radius))


if __name__ == '__main__':
    main()`