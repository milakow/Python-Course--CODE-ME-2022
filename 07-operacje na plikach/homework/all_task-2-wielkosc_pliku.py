#Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.
import os

size = os.path.getsize(r'C:\Users\Kamila\PycharmProjects\pythonProjectCM\07-operacje na plikach\cytaty.txt')

print(f'Wielkość pliku wynosi {size} bajtów')
