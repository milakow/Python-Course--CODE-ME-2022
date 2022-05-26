number = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# print(len(number))
# numbers = number.split
len_of_each_part = int(len(number) / 3)
print(len_of_each_part)

while n in range(4):
    new_list = number.pop(len_of_each_part)
    print(new_list)
