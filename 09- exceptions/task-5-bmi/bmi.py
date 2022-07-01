from math import ceil


def calc_bmi(weight, height):
    return ceil(weight / ((height * 0.01) ** 2))


def get_bmi_status(bmi):
    if bmi < 18.5:
        return ("underweight")
    elif 18.5 <= bmi <= 24.9:
        return ("healthy_weight")
    elif 25 <= bmi < 29.9:
        return ("overweight")
    else:
        return ("obesity")
