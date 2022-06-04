example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]


new_example_tuple = tuple(set(example_list))
# print(new_example_tuple)

new_example_list = list(new_example_tuple)
new_example_list2 = sorted(new_example_list)
print(f'Najmniejsza liczba to {new_example_list2[0]}, a największa {new_example_list2[-1]}')


# for number in example_list:
#     if example_list.count(number) > 1:
#         example_list.remove(number)
#     print(number)