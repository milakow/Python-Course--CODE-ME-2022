password = input('Podaj hasło: ')

if len(password) < 8:
    print('Hasło jest zbyt krótkie. Powinno zawierać co najmniej 8 znaków.')

if password.isalnum() and (password.isalpha() or password.isdigit()):
    print('Hasło powinno zawierać cyfry i litery.')

if password.isalnum and password.islower():
    print('Hasło zawiera tylko małe litery. Powinno zawierać co najmniej 1 dużą literę')

if password.isalnum and password.isupper():
    print('Hasło zawiera tylko duże litery. Powinno zawierać  co najmniej 1 dużą literę')



