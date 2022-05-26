users_elements = input('Podaj parzystą listę elementów oddzielonych przecinkiem: ')

users_elements = users_elements.split(',')
mid_element = int(len(users_elements)/2)

if len(users_elements) % 2 != 0:
    print('Nie podałeś parzystej ilości elementów w liście.')
elif users_elements[mid_element-1] == users_elements[mid_element]:
    print('Dwa środkowe elementy są takie same.')
else:
    print('Dwa środkowe elementy różnią się od siebie.')
