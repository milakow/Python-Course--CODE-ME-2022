from math import ceil
weight_in_kg = float((input("Podaj wagę w kg: ")))
height_in_m = float((input("Podaj wzrost w m: ")))

bmi = ceil(weight_in_kg / (height_in_m**2))

#na podstawie https://www.medicover.pl/kalkulator/bmi/
if bmi < 18.5:
    print("niedowaga")
elif 18.5 <= bmi <= 24.9:
    print("waga prawidłowa")
elif 25 <= bmi < 29.9:
    print("overweight.txt")
else:
    print("otyłość")
