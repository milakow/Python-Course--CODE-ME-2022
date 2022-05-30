import random

comp_choice = random.randint(1, 100)
# print(comp_choice)

for i in range(6):
    user_choice = int(input('Pick a number from 1 to 100 '))
    if not 0 < user_choice < 101:
        print('You have picked the number from wrong range.')
    elif user_choice == comp_choice:
        print(f'Perfect. You did it! The correct number is {comp_choice}')
        break
    elif comp_choice - 10 <= user_choice <= comp_choice + 10:
        print('Warm. You\'re so close.')
    else:
        print('Cold. Try one more time.')
    continue

if user_choice != comp_choice:
    print(f'You have lost. Try another time. The correct number is {comp_choice}.')



