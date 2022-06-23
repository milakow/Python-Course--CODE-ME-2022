def sum_natural(numbers):
    sum_num = 0

    for i in range(1, numbers + 1):
        sum_num += i
    return sum_num

# print(sum_natural(10))

def sum_natural_while(n):
    sum_num = 0

    while n > 0:
        sum_num += n
        n -= 1

    return sum_num

print(sum_natural_while(10))
