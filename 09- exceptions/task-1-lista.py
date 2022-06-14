elements = [12, 'basia', 5.5, True]

for item in elements:
    try:
        result = 10 / item
        print(result)
    except TypeError as val_error:
        print('Pojawił się błąd. Wyjątek: ', val_error)
