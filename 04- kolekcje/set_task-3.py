tuple_1 = (1, 3, 4, 6, 9, 0)
tuple_2 = ("pies", "kot", "królik", "chomik", "jaszczurka", "pająk", 1, 3, 4)

#print(tuple_1[::2])
#print(tuple_2[1::2])

effect = tuple_1[::2] + tuple_2[1::2]
effect = list(effect)
print(effect)

result_set = set(effect)
print(result_set)