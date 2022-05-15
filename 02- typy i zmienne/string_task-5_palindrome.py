palindrome = input('Podaj palindrom: ')
palindrome = palindrome.replace(" ", "")

print(palindrome == palindrome[::-1])