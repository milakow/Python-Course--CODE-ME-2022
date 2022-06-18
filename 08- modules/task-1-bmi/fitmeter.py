#Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
import bmi

def main():
    weight_in_kg = float((input("Podaj wagę w kg: ")))
    height_in_m = float((input("Podaj wzrost w m: ")))  # mozna zabezpieczyc while

    result = bmi.calculate_bmi(weight_in_kg, height_in_m)
    print('Twoje BMI wynosi: ', bmi.get_bmi_status(result))
    print(bmi.read(result))

if __name__ == '__main__':
    main()