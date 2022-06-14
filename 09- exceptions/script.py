print('************')
x = 35 - 6
print(x)
# result = 10 / 0


try:
    ppl = int(input('Podaj liczbę osób: '))
    result = 10 / ppl
except ZeroDivisionError as err:
    print('Pojawił się błąd. Twój wyjątek to', err)
    result = 10
except ValueError:
    print('Nowy błąąąąąąd!')
    result = 10

print(result)
print('the end')

