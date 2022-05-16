txt = 'aBarKadabra123'
count_low = 0
count_upp = 0
count_num = 0

for letter in txt:
    print(letter)

    if letter.islower():
        count_low +=1
        continue

    if letter.isupper():
        count_upp +=1
        continue

    if letter.isdigit():
        count_num +=1

print (f'Text')
