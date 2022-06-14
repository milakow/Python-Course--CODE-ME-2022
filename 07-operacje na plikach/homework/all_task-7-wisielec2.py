# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy. Rozgrywka powinna być maksymalnie intuicyjna.
import random


def pick_cat(lines, user_cat):
    while True:
        category = input('Pick a category: fruits, animals, countries: ').lower()
        print(category)
        if not (category.isalpha() and (category == 'fruits' or category == 'animals' or category == 'countries')):
            print('You entered incorrect category. Choose again: ')
        else:
            break

    with open('wisielec', 'r') as fopen:
        lines = str(fopen.readlines())
    lines = lines.split('.')
    category1 = lines[1]
    category2 = lines[3]
    category3 = lines[5]

    print(category1)
    if user_cat == 'f':
        return category1
    elif user_cat == 'a':
        return category2
    else:
        return category3


def pick_password(lines, user_cat):
    password_list = ['cracow']
    chosen_password = random.choice(password_list)
    return chosen_password
    # if user_cat == 'f':
    #     return category1
    # elif user_cat == 'a':
    #     return category2
    # else:
    #     return category3


# def guess_password(num_of_rounds, chosen_password):
#     chosen_password_list = list(chosen_password)
#     password_line = []
#     for letter in range(len(chosen_password_list)):
#         password_line.append("_")
#
#     print(*password_line)
#
#     for rnd in range(num_of_rounds):
#         user_choice = str(input('Pick a letter: '))
#         if not user_choice.isalpha():
#             print('Podałeś zły znak.')
#             continue
#         index = 0
#         if password_line.count('_') == 0:
#             print('You have managed to win!')
#             break
#
#         if len(user_choice) == 1:
#             if chosen_password.find(user_choice) != -1:
#                 for letter in chosen_password_list:
#                     if user_choice == letter:
#                         password_line[index] = letter
#                     index += 1
#             else:
#                 print('Bad choice.')
#         else:
#             if user_choice == chosen_password:
#                 print('Exactly! You\'re a winner!')
#                 break
#             else:
#                 print('You did not guess.')
#         print(*password_line)
#         if rnd == num_of_rounds - 1:
#             print('Unfortunately you lost. Try another time.')
#
#
# def main():
#     num_of_rounds = pick_no_of_chances()
#     chosen_password = pick_password()
#     guess_password(num_of_rounds, chosen_password)
#
#
# main()
