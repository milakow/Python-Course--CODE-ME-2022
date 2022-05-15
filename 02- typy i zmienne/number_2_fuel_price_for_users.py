consumption = float(input ("Podaj średnie spalanie na 100 km (w l): "))

distance = float(input("Podaj długość trasy (w km): "))

fuel_price = float(input("Podaj cenę paliwa (w zł): "))

trip_price = distance * consumption / 100 * fuel_price

print ("Koszt wyprawy wynosi:", round(trip_price, 2), "zł")