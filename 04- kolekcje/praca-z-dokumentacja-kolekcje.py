num_list = [1, 2.3, 2, 4, 2, 7, 2, 2]

#1 metoda, która utworzy kopię listy
num_list_copy = num_list.copy()
print(num_list_copy)

#2 metoda, ktora posortuje elementy na liście
num_list.sort()
print(num_list)


#3 metoda, która usunie wszystkie elementy z listy
num_list2 = num_list.clear()
print(num_list2)

my_list = [ 1, 2, 6, 2, 5, 2]
#4 policzy wystąpienia takiego samego elementu na liście
print(my_list.count(2))

#5 zsumuje liczby na liście
my_list_sum = sum(my_list)
print(my_list_sum)
