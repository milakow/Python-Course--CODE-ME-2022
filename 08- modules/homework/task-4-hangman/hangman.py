import random


def read():
    with open('wisielec', 'r') as fopen:
        lines = fopen.readlines()
    return lines


def pick_cat():
    while True:
        category = input('Pick a category: fruits, animals, countries: ').lower()
        if not (category.isalpha() and (category == 'fruits' or category == 'animals' or category == 'countries')):
            print('You entered incorrect category. Choose again.')
        else:
            break
    return category


def pick_password(category, lines):
    if category == 'fruits':
        password = random.choice(lines[0].split(','))
        return password
    elif category == 'animals':
        password = random.choice(lines[1].split(','))
        return password
    elif category == 'countries':
        password = random.choice(lines[2].split(','))
        return password
    else:
        print('You picked incorrect category')


def guess_password(num_of_rounds, chosen_password):
    chosen_password_list = list(chosen_password)
    password_line = []

    for letter in range(len(chosen_password_list)):
        password_line.append("_")
    print(*password_line)

    for rnd in range(num_of_rounds):
        user_choice = str(input('Pick a letter: '))
        if not user_choice.isalpha():
            print('Podałeś zły znak.')
            continue
        index = 0

        if len(user_choice) == 1:
            if chosen_password.find(user_choice) != -1:
                for letter in chosen_password_list:
                    if user_choice == letter:
                        password_line[index] = letter
                    index += 1
            else:
                print('Bad choice.')
        else:
            if user_choice == chosen_password:
                print('Exactly! You\'re a winner!')
                break
            else:
                print('You did not guess.')
        print(*password_line)
        if password_line.count('_') == 0:
            print('You have managed to win!')
            break
        if rnd == num_of_rounds - 1:
            print('Unfortunately you lost. Try another time.')
            break
