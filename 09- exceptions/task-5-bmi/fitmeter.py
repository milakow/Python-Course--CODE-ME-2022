#W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float. Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.
import bmi

def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()
    return advice

def get_value(user_data, min_max):
    while True:
        try:
            value = float(input(user_data))
            minimum, maximum = min_max

            if not (value in range(minimum, maximum)):
                raise ValueError
        except TypeError:
            print('Type error. Try again.')
        except ValueError:
            print('Value error. Try again.')
        else:
            return value


def main():
    w = get_value(("Enter weight in kg: "), (30, 200))
    h = get_value(("Enter height in cm: "), (140, 230))

    result = bmi.calc_bmi(w, h)
    print(result)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)


if __name__ == '__main__':
    main()
