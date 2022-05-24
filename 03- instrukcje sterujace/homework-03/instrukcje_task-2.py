txt = input("Enter any text: ")

# first way
for index in range(len(txt))[1::2]:
    print(txt[index], end='')
print()

# second way
text = input("Enter another text: ")
print(text[1::2])
