import random

comp_choice = random.randint(1, 100)
print(comp_choice)

for i in range(6):
    user_choice = int(input('Wybierz liczbę od 1 do 100: '))
    if not 0 < user_choice < 101:
        print('Podałeś zły zakres.')
    elif user_choice == comp_choice:
        print(f'Doskonale. Trafiłeś! Wybrana liczba to {comp_choice}')
        break
    elif comp_choice - 10 <= user_choice <= comp_choice + 10:
        print('Ciepło. Jesteś już blisko.')
    else:
        print('Zimno. Próbuj dalej.')
    continue

if user_choice != comp_choice:
    print(f'Przegrałeś. Spróbuj ponownie. Wybrana liczba to {comp_choice}.')



