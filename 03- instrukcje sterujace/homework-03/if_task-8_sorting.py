num1 = float(input("Podaj pierwszą dowoloną liczbę: "))
num2 = float(input("Podaj drugą dowolną liczbę: "))
num3 = float(input("Podaj trzecią dowolną liczbę: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print("Największa liczba to", num1, "a kolejność to: ", num1, num2, num3)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print("Największa liczba to", num1, "a kolejność to: ", num1, num3, num2)
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("Największa liczba to", num2, "a kolejność to: ", num2, num1, num3)
elif num2 > num1 and num2 > num3 and num3 > num1:
    print("Największa liczba to", num2, "a kolejność to: ", num2, num3, num1)
elif num3 > num1 and num3 > num2 and num1 > num2:
    print("Największa liczba to", num3, "a kolejność to: ", num3, num1, num2)
else:
    print("Największa liczba to", num3, "a kolejność to: ", num3, num2, num1)
