def find_max(num1, num2, num3):
    if num1 >= num2 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def main():
    number1 = float(input('Podaj pierwszą liczbę: '))
    number2 = float(input('Podaj drugą liczbę: '))
    number3 = float(input('Podaj trzecią liczbę: '))
    result = find_max(number1, number2, number3)
    print(f'Największa liczba to: {result}')

main()
