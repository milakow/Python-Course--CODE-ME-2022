#Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
def get_int(num):
    if num.isalpha():
        print(f'{num} to nie liczba')
    else:
        return int(num)

def is_number(num_list):
    int_numbers = list(map(get_int, num_list))
    return int_numbers

def get_filter_int(num):
    try:
        if num is None:
            raise ValueError
            return False
        else:
            return True
    except ValueError:
        with open('errors.txt', 'a') as f:
            f.write(f'error is: ValueError\n')

def count_average(num_list):
    return sum(num_list)/len(num_list)

def main():
    user_numbers = input('Enter numbers separated by a comma: ').replace(' ', '')
    num_list = user_numbers.split(',')

    int_num = is_number(num_list)
    filter_int = list(filter(get_filter_int, int_num))
    average = count_average(filter_int)
    print(average)

if __name__ == '__main__':
    main()
