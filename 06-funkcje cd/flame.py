#FLAMES to popularna gra, której nazwa postała od akronimu: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. Choć gra nie pozwala dokładnie przewidzieć przyszłości to może sprawdzić się jako andrzejkowa wróżba.

def get_first_name():
    name = input('Pick first name: ')
    if not name.isalpha():
        raise TypeError
    else:
        return name

def get_second_name():
    name = input('Pick second name: ')
    if not name.isalpha():
        raise TypeError
    else:
        return name

def delete_letters(first_name, second_name):
    for letter in first_name:
        for let in second_name:
            if letter == let:
                # print(letter)
                first_name = first_name.replace(letter, '')
                second_name = second_name.replace(let, '')
    return first_name, second_name

def show_meaning(number):
    if number % 5 == 1:
        return 'Friendship'
    elif number % 5 == 2:
        return 'Love'
    elif number % 5 == 3:
        return 'Affection'
    elif number % 5 == 4:
        return 'Marriage'
    elif number % 5 == 0:
        return 'Enemies'
    else:
        return 'I dont know meaning'

def main():
    first_name = get_first_name()
    second_name = get_second_name()
    f_name, s_name = delete_letters(first_name, second_name)
    number = len(f_name) + len(s_name)
    print(f_name, s_name, number)
    # print(f'length of first name: {len(f_name)}')
    # print(f'length of second name: {len(s_name)}')
    meaning = show_meaning(number)
    print(f' The meaning for {first_name} and {second_name} is {meaning}.')


if __name__ == '__main__':
    main()
