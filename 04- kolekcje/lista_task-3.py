user_list = (input("Podaj listę liczb calkowitych podzielonych przecinkiem : "))

user_list = user_list.split(", ")
print(user_list)

print("Czy pierwszy i ostatni są takie same? -->", user_list[0] == user_list[-1])
