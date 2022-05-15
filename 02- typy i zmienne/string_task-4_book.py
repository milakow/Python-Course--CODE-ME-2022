title_of_book = input('Podaj tytuł książki: ')

author_name = input('Podaj nazwisko autora książki: ')

number_of_pages = input('Podaj liczbę stron książki: ')

print(title_of_book.isalpha())
print(author_name.isalpha())
print(number_of_pages.isdigit())

title_of_book = title_of_book.title()
print(title_of_book)

author_name = author_name.capitalize()
print(author_name)

book = title_of_book + " " + author_name + " " + number_of_pages
print(book)

print(len(book))