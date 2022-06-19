# Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.
from chances import pick_no_of_chances
from hangman import read, pick_password, pick_cat, guess_password

def main():
    num_of_rounds = pick_no_of_chances()
    category = pick_cat()
    lines = read()
    chosen_password = pick_password(category, lines)
    chosen_password = chosen_password.replace(" ", "")
    guess_password(num_of_rounds, chosen_password)


main()
