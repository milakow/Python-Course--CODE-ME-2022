# row = 10
# col = 10
product = []
# multiplication_table = [[product]*row]*col
# print(multiplication_table)

for number in range(1, 11):
    for item in range(1, 11):
        product = number * item
        print(product, end=" ")
        continue
    # new_product = product.extend()
    print()