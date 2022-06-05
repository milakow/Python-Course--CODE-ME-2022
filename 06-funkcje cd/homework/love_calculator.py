def count_letter(word):
    letter_counter = {}
    set_of_letters = {}
    for letter in word:
        counter = word.count(letter)
        set_of_letters = set(letter)
        letter_counter = dict.fromkeys(letter)
        print(letter_counter)
        if counter > 1:
            letter_counter[letter] += 1
        else:
            letter_counter = 1
    return letter_counter


def main():
    name_1 = input('Enter first name: ').lower()
    name_2 = input('Enter second name: ').lower()
    word_for_calculator = name_1 + 'loves' + name_2
    print(word_for_calculator)

    print(count_letter(word_for_calculator))


main()

