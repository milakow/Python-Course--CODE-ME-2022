opinion1 = int(input('Podaj opinię w skali 1- 10 o książce (>7 - bdb, ocena 5-7 przeciętna, <=4- nie warta uwagi): '))
opinion2 = int(input('Podaj opinię w skali 1- 10 o książce (>7 - bdb, ocena 5-7 przeciętna, <=4- nie warta uwagi): '))
opinion3 = int(input('Podaj opinię w skali 1- 10 o książce (>7 - bdb, ocena 5-7 przeciętna, <=4- nie warta uwagi): '))

average_opinion = (opinion1 + opinion2 + opinion3) / 3

if average_opinion > 7:
    print('Książka jest bardzo dobra.')
elif average_opinion >= 5:
    print('Książla jest przeciątna.')
else:
    print('Książka nie jest warta uwagi.')
