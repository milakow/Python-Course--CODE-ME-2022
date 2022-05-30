def check_num(user_list, number):
    check_number = user_list.count(number)
    return check_number


def main():
    user_numbers = input('Enter a list of numbers separated by a comma: ')
    number = str(input('Pick a number to check: '))
    result = check_num(user_numbers, number)

    print((f'Yes, the number {number} is in the given range') if result >= 1 else (f'No, number {number} is out of given range.'))

    # if result >= 1:
    #     print(f'Yes, the number {number} is in the given range')
    # else:
    #     print(f'No, number {number} is out of given range.')

main()

