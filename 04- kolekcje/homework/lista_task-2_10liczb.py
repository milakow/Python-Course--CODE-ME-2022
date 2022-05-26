ten_numbers = []

for num in range(10):
    num = int(input('Podaj liczbę: '))
    if num % 2 == 1:
        ten_numbers.append(num)

print(ten_numbers)


