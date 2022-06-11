import random


def get_comp_choice():
    comp_choice = ["k", "p", "n"]
    computers_figure = random.choice(comp_choice)
    return computers_figure


def get_user_choice(num_of_rounds):
    user_figure = input("Podaj jedną z 3 figur: kamień (k)/ papier(p)/ nożyce(n)/ koniec: ")
    return user_figure


def main():
    num_of_rounds = int(input('Podaj ilość rund: '))
    user_points = 0
    computer_points = 0
    for i in range(num_of_rounds):
        computers_figure = get_comp_choice()
        user_figure = get_user_choice(num_of_rounds)
        if not (user_figure == 'k' or user_figure == 'p' or user_figure == 'n'):
            print('Podałeś niewłaściwą figurę. Tracisz rundę.')

        if user_figure == 'koniec':
            print(f'Dzięki za grę. Zdobyłeś {user_points} punktów.')
            break

        elif user_figure == computers_figure:
            print(f'Remis! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

        elif (user_figure == "p" and computers_figure == 'k') or (user_figure == "n" and computers_figure == 'p') or (
                user_figure == 'k' and computers_figure == 'n'):
            user_points += 1
            print(f'Wygrałeś tą rundę! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

        else:
            computer_points += 1
            print(f'Runda przegrana. Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

    if user_points > computer_points:
        print(f'Koniec. Gratulacje, wygrałeś! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')
    elif user_points == computer_points:
        print(f'Koniec. Remis! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')
    else:
        print(
            f'Koniec. Przegrałeś, spróbuj jeszcze raz! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')


main()
