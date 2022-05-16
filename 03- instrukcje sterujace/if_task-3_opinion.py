opinion1 = int(input('Podaj opinię w skali od 1 do 10 o książce uwzględniając, że: ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi. Jaka jest twoja opinia?: '))
opinion2 = int(input('Podaj opinię w skali od 1 do 10 o książce uwzględniając, że: ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi. Jaka jest twoja opinia?: '))
opinion3 = int(input('Podaj opinię w skali od 1 do 10 o książce uwzględniając, że: ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi. Jaka jest twoja opinia?: '))

average_opinion = (opinion1 + opinion2 + opinion3) / 3

if average_opinion > 7:
    print ('Książka jest bardzo dobra.')
elif average_opinion >=5:
    print ('Książla jest przeciątna.')
else:
    print('Książka nie jest warta uwagi.')