#Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.
def clear_content(txt):
    for char in '!,..-();—':
        txt = txt.replace(char, '')
    txt = txt.replace('\n', ' ')
    return txt


def find_longest(text):
    longest = ''
    for word in text:
        if len(word) > len(longest):
            longest = word

    return longest


def main():
    with open('pan_tadeusz.txt', encoding='utf-8') as f:
        content = f.read()

    content = clear_content(content)
    content = content.split()
    # print(content)
    longest_word = find_longest(content)
    print(longest_word)


main()

