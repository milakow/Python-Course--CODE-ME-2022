#Utwórz generator dowolnego typu np. generator zdań, (tweetów czy konferencji.) Dane wejściowe pobierz z pliku csv (plik csv możesz traktować jako plik txt ze znanym znakiem podziału), który będzie przechowywał dane potrzebne do generowania.
import random

def read():
    with open('words.txt', encoding='utf-8') as fopen:
        return fopen.readlines()

def pick_subject(words):
    return random.choice(words[0].split(','))

def pick_time(words):
    return random.choice(words[1].split(','))

def pick_verb(words):
    return random.choice(words[2].split(','))

def pick_place(words):
    return random.choice(words[3].split(','))

def pick_aim(words):
    return random.choice(words[4].split(','))

def pick_purpose(words):
    return random.choice(words[5].split(','))


def main():
    content = read()
    my_list = []
    for words in content:
        my_list.append(words.replace('\n', ''))
    print(pick_subject(my_list), pick_time(my_list), pick_verb(my_list), pick_place(my_list), pick_aim(my_list), pick_purpose(my_list) + '.')


if __name__ == '__main__':
    main()
