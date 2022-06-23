graph = {
    'dom': ['kosciol', 'bar', 'szkola'],
    'szkola': ['dom', 'szpital'],
    'kosciol': ['dom', 'bar', 'kino'],
    'bar': ['kosciol', 'dom', 'szpital'],
    'szpital': ['szkola', 'bar', 'kino', 'teatr'],
    'kino': ['kosciol', 'szpital', 'teatr'],
    'teatr': ['kino', 'szpital']

}

for place in graph:
    for row in graph(place):
        print(place, '-', row)


# buildings = {
#     0: 'house',
#     1: 'school',
#     2: 'church',
#     3: 'bar',
#     4: 'hospital',
#     5: 'cinema',
#     6: 'theater'
# }
#
# matrix = [
#     [0,1,1,1,0,0,0],
#     [1,0,0,0,1,0,0],
#     [1,0,0,1,1,1,0],
#     [1,0,1,0,1,0,0],
#     [0,1,1,1,0,1,1],
#     [1,0,1,0,1,0,1],
#     [0,1,0,0,1,1,1]
# ]
#
#
# for id_row, row in enumerate(matrix):
#     for id_col, col in enumerate(row):
#         if col == 1:
#             print(buildings[id_row], '---->', buildings[id_col])

