from math import ceil

hours_to_learn = 75
my_free_hours_pday = 2
days = 7

hours_in_week = my_free_hours_pday * days
result = hours_to_learn/hours_in_week
result = ceil(result)

print("Nauka zajmie mi", result, "tygodni")
