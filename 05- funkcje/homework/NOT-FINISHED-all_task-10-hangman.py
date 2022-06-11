import random


def get_comp_choice():
    password_list = ['cracow','prague', 'dubrovnik', 'barcelona', 'bratislava', 'lisbon', 'budapest' ]
    chosen_password = random.choice(password_list)
    return chosen_password


def get_list_of_password(chosen_password):
    chosen_password_list = list(chosen_password)  ##1/2
    password_line = []
    for letter in range(len(chosen_password_list)):
        password_line.append("_")
    return password_line


def change_char(user_choice):



def main():
    num_of_rounds = 10
    print(f'Welcome in Hangman game. You have {num_of_rounds} rounds to try to win with me :)\n')
    chosen_password = get_comp_choice()
    chosen_password_list = list(chosen_password)   ##2/2
    for rnd in range(num_of_rounds):
        password_line = get_list_of_password(chosen_password)
        print(*password_line)
        user_choice = str(input('Pick a letter: '))
        if not user_choice.isalpha():
            print('Podałeś zły znak.')
            continue
        index = 0
        if len(user_choice) == 1:
            if not chosen_password.find(user_choice) == -1:
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
        if rnd == num_of_rounds - 1:
            print('Unfortunately you lost. Try another time.')


main()
