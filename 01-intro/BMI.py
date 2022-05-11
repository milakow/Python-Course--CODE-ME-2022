from math import ceil
weight_in_kg = float((input("Podaj wagę w kg: ")))
height_in_m = float((input("Podaj wzrost w m: ")))

bmi = ceil(weight_in_kg / (height_in_m**2))
print("Your BMI is:", bmi)

