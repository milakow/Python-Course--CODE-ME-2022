#Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
elements = [12, 'basia', 5.5, True]

for item in elements:
    try:
        result = 10 / item
        print(result)
    except TypeError as val_error:
        print('Pojawił się błąd. Wyjątek: ', val_error)
