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


def main():
    weight_in_kg = float((input("Podaj wagę w kg: ")))
    height_in_m = float((input("Podaj wzrost w m: ")))  # mozna zabezpieczyc while

    result = calculate_bmi(weight_in_kg, height_in_m)
    print('Twoje BMI wynosi: ', get_bmi_status(result))


main()

# weight_in_kg = float((input("Podaj wagę w kg: ")))
# height_in_m = float((input("Podaj wzrost w m: ")))
#
# result = bmi(weight_in_kg, height_in_m)
#
# # na podstawie https://www.medicover.pl/kalkulator/bmi/
# if result < 18.5:
#     print("niedowaga")
# elif 18.5 <= result <= 24.9:
#     print("waga prawidłowa")
# elif 25 <= result < 29.9:
#     print("overweight.txt")
# else:
#     print("otyłość")
