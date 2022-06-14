import random


def get_comp_choice():
    password_list = ['lisbon', 'cracow','prague', 'dubrovnik', 'barcelona', 'bratislava', 'budapest']
    chosen_password = random.choice(password_list)
    return chosen_password


def get_list_of_password(chosen_password):
    chosen_password_list = list(chosen_password)
    password_line = []
    for letter in range(len(chosen_password_list)):
        password_line.append("_")
    return password_line


def guess_password(chosen_password, num_of_rounds):
    chosen_password_list = list(chosen_password)
    password_line = get_list_of_password(chosen_password)
    for rnd in range(num_of_rounds):
        user_choice = str(input('Pick a letter: '))
        if not user_choice.isalpha():
            print('Podałeś zły znak.')
            continue
        if len(user_choice) == 1:
            if not chosen_password.find(user_choice) == -1:
                index = 0
                for letter in chosen_password_list:
                    if user_choice == letter:
                        password_line[index] = letter
                    index += 1
            else:
                print('Bad choice.')

            if password_line.count("_") == 0:
                print('Wow! Very impressive. You did it!')
                break
        else:
            if user_choice == chosen_password:
                print('Exactly! You\'re a winner!')
                break
            else:
                print('You did not guess.')
        print(*password_line)

        if rnd == num_of_rounds - 1:
            print('Unfortunately you lost. Try another time.')


def main():
    num_of_rounds = 10
    print(f'Welcome in Hangman game. You have {num_of_rounds} rounds to try to win with me :)\n')
    chosen_password = get_comp_choice()
    print(*get_list_of_password(chosen_password))
    guess_password(chosen_password, num_of_rounds)


main()
