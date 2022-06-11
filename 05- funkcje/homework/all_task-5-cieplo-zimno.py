import random


def get_computer_choice():
    comp_choice = random.randint(1, 100)
    return comp_choice


def get_user_choice():
    user_idea = int(input('Wybierz liczbę od 1 do 100: '))
    return user_idea


def main():
    password = get_computer_choice()

    rnd = int(input('Pick a number of rounds: '))
    for chance in range(rnd):
        variable = get_user_choice()

        if not 0 < variable < 101:
            print('You have picked the number from wrong range.')
        elif variable == password:
            print('Amazing. You won!!!')
        elif password -10 <= variable <= password + 10:
            print('Warm. You\'re so close.')
        else:
            print('Cold. Try one more time. ')
    if variable != password:
        print(f'You have lost. Try another time. The correct number is {password}.')


main()

