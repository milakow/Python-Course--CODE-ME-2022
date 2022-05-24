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

num = input("Podaj liczbę od 1 do 20 ->")
num = int(num)
numbers = (1, 3, 4, 20, 13, 16, 9)

if num in numbers:
    print('znalazłem, pod indexem:', numbers.index(num))
else:
    print('nie ma takie liczby')