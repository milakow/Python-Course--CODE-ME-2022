from math import ceil


def calculate_bmi(weight, height):
    return ceil(weight / (height ** 2))


def get_bmi_status(bmi):
    if bmi < 18.5:
        return ("niedowaga")
    elif 18.5 <= bmi <= 24.9:
        return ("waga prawidłowa")
    elif 25 <= bmi < 29.9:
        return ("overweight.txt")
    else:
        return ("otyłość")


def read(result):
    if result < 18.5:
        with open('niedowaga.txt', encoding='utf-8') as fopen:
            content = fopen.readlines()
        return content

    elif 18.5 <= result <= 24.9:
        with open('waga_prawidlowa.txt', encoding='utf-8') as fopen:
            content = fopen.readlines()
        return content

    elif 25 <= result < 29.9:
        with open('nadwaga.txt', encoding='utf-8') as fopen:
            content = fopen.readlines()
        return content

    else:
        with open('otylosc.txt', encoding='utf-8') as fopen:
            content = fopen.readlines()
        return content


