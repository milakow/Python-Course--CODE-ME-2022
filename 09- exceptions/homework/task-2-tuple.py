#Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd
elements = (12, 3.5, 6.0, 5, 12, 0, -5, -12.9, 90, 1234)
elements_list = list(elements)

try:
    user_id = int(input('Pick an index from 1 to 10: '))
    user_value = float(input('Pick a value for mentioned index: '))
    if user_id >= 1 or user_id <= 10:
        pass
    else:
        print(f'Error. {user_id} is not in range.')
    for index, value in enumerate(elements_list):
        if user_id - 1 == index:
            elements_list.pop(user_id - 1)
            elements_list.insert(user_id - 1, user_value)

except ValueError as e:
    print('Attention: ', e)
except TypeError as e:
    print('Error: ', e)

new_elements = tuple(elements_list)
print(new_elements)
