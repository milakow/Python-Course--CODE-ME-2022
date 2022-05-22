'''
numbers = 1, 5, 3, 7, 4, 6
example = int(input("Podaj liczbę całkowitą od 1 do 10: "))
flag = False

for i, v in enumerate(numbers):
    if example == v:
        print('znalazłem pod indeksem:', i)
        flag = True
        break

if not flag:
    print("nie ma takiej liczby")
'''

num = input("")