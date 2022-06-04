user_num = int(input('Pick a random number: '))
num_val = 0
numbers = {}

for number in range(1, user_num + 1):
    num_val = number ** 2
    numbers[number] = num_val
print(numbers)



#druga metoda- tworzy wiele słowników
# for number in range(1, user_num + 1):
#     num_val = number ** 2
#     numbers = dict.fromkeys(str(number), num_val)  #python nie przyjmuje mi klucza jako int, musiałam zamienić na str
# print(numbers)



