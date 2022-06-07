# f = open('example')
# print(f.readlines())
# f.close()

# with open('example') as fp:
#     content = fp.readlines()
#
# print(content)
# for line in content:
#     print(line)
#
#
# with open('pan_tadeusz.txt', 'w') as f:
#     f.write('alamakota')

# with open('plik.txt', 'r') as fopen:
#   content = fopen.readlines()
#
# for l in lines):
#   print("Line : " + l )

#zapisywanie do pliku
#1opcja
# with open('save.txt', 'w') as f:
#     f.write('Line 1')
#     f.write('Line 2')
#     f.write('Line 3')
#     f.write('Line 4')
#2opcja- poprawienie
# with open('save.txt', 'w') as f:
#   f.write('Line 1\n')
#   f.write('Line 2\n')
#   f.write('Line 3\n')
#   f.write('Line 4\n')
#   f.write('The end!')

#wypisywanie elementów z listy
# equipment_for_trip = ['compass', 'flashlight', 'bag', 'water']
# #1 opcja
# with open('trip.txt', 'w') as f:
#     for i in equipment_for_trip:
#         f.write(i + "\n")
#
# #2 opcja
# equipment_str = '\n'.join(equipment_for_trip)
#
# with open('trip.txt', 'w') as f:
#     f.write(equipment_str)

