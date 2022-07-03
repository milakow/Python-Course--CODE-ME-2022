#Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
# num = ['5']
# print(type(num))
# print(int(num))

user_numbers = input('Enter numbers separated by a comma: ')
list_user_num = user_numbers.split(',')
for number in list_user_num:
    int_num = int(number)
    print(int_num)


# int_user_num = int(user_numbers)
# print(int_user_num)
