txt = "1234"
txt2 = "fvgbhnjmk2345"

#1 jak sprawdzic czy ciag znakow sklada sie tylko z cyfr
    #1 str.isdigit()
print(f'Ciąg{txt} zawiera same cyfry ->', txt.isdigit())
print(txt2.isdigit())

#2jak wyswietlic wysrodkowany tekst o zadanej szerokosci i dodatkowo puste miejsca wypelnic np. gwiazdka: '***mata***'
    #2 str.center(width[, fillchar])
txt='mata'
centered_txt = txt.center (10, '*')
print (centered_txt)

#3 Jaka metoda usunie znaki tylko z prawej strony
    #3 str.lstrip([chars])
url = 'ww.example.com'
new_url = url.lstrip('w.')
print(new_url)

dna = 'AAATTTGGCCAAAA'
cleaned_dna = dna.rstrip ('A')
print(cleaned_dna)

#4 (2 metody) jak sprawdzic czy ciag ma co najmniej jedna duza litere
    #4 str.find(sub[, start[, end]])¶
    #4 str.islower()

password = 'AdminAdminTakNieRobHasla'
includes_at_least_1_upper = password.isalpha() and (not password.islower() and not password.isupper())
print(includes_at_least_1_upper)

#5 policzy ile razy zadany ciag znakow np. ('na') wystpalik w ciagu znakow ('banana'=2)
    #5 str.count(sub[, start[, end]])

fruit = 'banana'
counter = fruit.count('na')
print(counter)
