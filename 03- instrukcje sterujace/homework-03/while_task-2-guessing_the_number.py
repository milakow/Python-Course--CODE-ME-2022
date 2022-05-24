secret_num = 7

user_num = int(input("Guess what number I picked from 0 to 20: "))

while secret_num != user_num:
    user_num = int(input("You missed. Choose another number: "))
print("Exactly!")
