# def

import random

comp_choice = ["k", "p", "n"]

num_of_rounds = int(input('Podaj ilość rund: '))
user_points = 0
computer_points = 0

while num_of_rounds > 0:
    for i in range(num_of_rounds):
        user_figure = input("Podaj jedną z 3 figur: kamień (k)/ papier(p)/ nożyce(n)/ koniec: ")
        if user_figure == 'koniec':
            break
        computers_figure = random.choice(comp_choice)

        if user_figure == computers_figure:
            print(f'Remis! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

        elif (user_figure == "p" and computers_figure == 'k') or (user_figure == "n" and computers_figure == 'p') or (
                user_figure == 'k' and computers_figure == 'n'):
            user_points += 1
            print(f'Wygrałeś tą rundę! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

        else:
            computer_points += 1
            print(f'Runda przegrana. Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')

    willing = input('Czy chcesz kontynuować grę? (tak/nie):')
    if willing == 'tak':
            continue
    else:
            break


if user_points > computer_points:
    print(f'Koniec. Gratulacje, wygrałeś! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')
elif user_points == computer_points:
    print(f'Koniec. Remis! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')
else:
    print(
        f'Koniec. Przegrałeś, spróbuj jeszcze raz! Wynik to {user_points} dla użytkownika do {computer_points} dla komputera.')