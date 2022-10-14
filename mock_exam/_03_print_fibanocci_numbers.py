"""
Print out all Fibonacci numbers smaller or equal to a given number
Given a positive number, print out all Fibonacci numbers smaller or equal to that number.
For example, given the number 11 the program should print out: 1 1 2 3 5 8
The next Fibonacci number would be 13 which is already larger than 11.
"""
def print_fibonacci_below_or_equal(maximum_integer):
    # We use a zero at the beginning because Wikipedia says so. Even though the assignment text says otherwise.
    list_of_fibonacci_numbers = [0, 1]
    
    if maximum_integer > 0:
        next_fibonacci = 1
        while next_fibonacci <= maximum_integer:
            # (list_of_fibonacci_numbers[-1] + list_of_fibonacci_numbers[-2]) > maximum_integer:

            list_of_fibonacci_numbers.append(next_fibonacci)
            next_fibonacci = list_of_fibonacci_numbers[-2] + next_fibonacci
            """
            if :
                break
            else:
                list_of_fibonacci_numbers.append(list_of_fibonacci_numbers[-1] + list_of_fibonacci_numbers[-2])
            """

        print(list_of_fibonacci_numbers)
    else:
        print(f"Wrong input! Number is negative or zero: {maximum_integer}.")

print_fibonacci_below_or_equal(11)

# ["a", "b"]
#   0    1   -> Coming from the left
#  -2   -1   -> Coming from the right (reverse indexing)
























def get_fibonacci(maximum_number) -> list:
    list_of_fibonacci_numbers = []
    if number <= maximum_number:

    else:
        return list_of_fibonacci_numbers