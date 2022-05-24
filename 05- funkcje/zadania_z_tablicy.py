# 1 Napisz funkcję, która pyta użytkownika o pary książka+ ocena i zapisuje je w programie
# title = input("Podaj tytuł książki: ")
# opinion = input("Podaj opinię książki w skali od 1 do 10: ")
# def book(title, opinion):
#     print(book())
# print(f'Książka o tytule {title} ma ocenę {opinion}')

# 1 Napisz funkcję, która pyta użytkownika o pary książka+ ocena i zapisuje je w programie/ drugie rozwiązanie
def add_book(books):
    title = input('Podaj ksiazke: ')
    grade = input(f'Oceń książkę {title}: ')
    books.append((title, grade))

#----
books = []
num = input('Ile ksiazek chcesz dodac? ')
for _ in range(num):
    add_book(books)

print(books)



# 2 Napisz funkcję, która zapyta o numer książki i wyświetli tytuł wraz z oceną
# book_number = input('Podaj numer książki: ')
#
#
# book_evaluation = {'title, opinion' : 'book_number'}
#
#
# def book_num (book_number, title, opinion):
#    print (title, opinion)


# 3 W prosty sposób obsłuż błąd użytkownika- użytkownik zapyta o numer w bazie, który nie istnieje


