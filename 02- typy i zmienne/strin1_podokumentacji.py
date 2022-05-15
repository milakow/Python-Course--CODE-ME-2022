#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu

word = 'dlugieslowo'
print(word[5])
print(len(word))
print(len(word)/2)
print(len(word)//2)
mid_index = len(word)//2
prev_id = mid_index - 1
next_id = mid_index + 1
print(next_id)
print(word[prev_id] + word[mid_index] + word[next_id])
print(word[prev_id : next_id + 1])