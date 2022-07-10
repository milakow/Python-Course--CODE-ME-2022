#Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.
from math import factorial


def pascal_triangle(number_of_rows):
    for row in range(number_of_rows):
        for single_space in range(number_of_rows - row + 10):
            print(end=" ")

        for row_elements in range(row + 1):
            print(factorial(row) // (factorial(row_elements) * factorial(row - row_elements)), end=" ")

        print("\n")

def main():
    rows_num = int(input('Pick a number of rows in Pascal triangle: '))
    pascal_triangle(rows_num)


if __name__ == '__main__':
    main()
