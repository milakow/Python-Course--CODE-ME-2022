def count_sequence(user_choice):
    first_number = 0
    next_number = 1
    # print(next_number)
    list_sum = [next_number]
    for numbers in range(user_choice-1):
        seq_sum = first_number + next_number
        first_number = next_number
        next_number = seq_sum
        list_sum.append(seq_sum)
    return list_sum









