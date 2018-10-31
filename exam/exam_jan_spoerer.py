def find_two_numbers(list_input, number):
    for i in range(0, len(list_input)):
        for j in range(i+1, len(list_input)):
            if list_input[i] + list_input[j] == number:
                return [list_input[i], list_input[j]]
    return []

first_sequence = [3, 4, 1, 7, 9, 17]
first_number = 8

print(find_two_numbers(first_sequence, first_number))  # [1, 7]

first_sequence = [1, 1, 1, 7, 9, 2]
first_number = 11

print(find_two_numbers(first_sequence, first_number))  # [9, 2]
