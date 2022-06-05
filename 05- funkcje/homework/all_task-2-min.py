def find_min_from_2_num(num1, num2):
    return num1 if num1 > num2 else num2


def find_min_from_3_num(num1, num2, num3):
    return find_min_from_2_num(num3, find_min_from_2_num(num1, num2))


def main():
    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))
    number3 = float(input('Enter third number: '))
    result = find_min_from_3_num(number3, number1, number2)
    print(result)

main()

