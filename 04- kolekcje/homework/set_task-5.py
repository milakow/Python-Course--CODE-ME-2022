S_test = {
    'dog',
    'cat',
    'hamster',
    'rabbit',
    'lizard'
}
#metoda discard nie wyswietla bledu, gdy element nie itnieje
S_test.discard('cat')
print(S_test)

#metoda remove wyswietla blad jesli dany element nie istnieje
S_test.remove('cat')
print(S_test)

