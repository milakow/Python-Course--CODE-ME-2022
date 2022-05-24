F = 0
while F <= 200:
    C = (5/9*(F-32))
    print(round(C, 2))
    F += 20

print('----------------')

for F in range(0, 201, 20):
    C = (5/9*(F-32))
    print(round(C, 2))
