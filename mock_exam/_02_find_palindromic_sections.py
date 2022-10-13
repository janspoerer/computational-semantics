"""
Find all 

palindromic sections (=sub string that is a palindrome)

of any given string longer than one.
A palindrome is a sequence that reads the same backwards as forwards. “Anna”, for
example is a palindrome.

The task is to find all palindromic sequences within any given string. 

The word “intellect” for example includes following palindromic sections:
“ll” intellect
“elle” intellect

"school school anna"
-> oo
-> oo
-> nn
-> anna
"""
from _01_palindrome import is_palindrome

def get_all_palidromes(input_string):
    list_of_strings = []

    # time_complexity_outer * time_complexity_inner * no_operations_inner = n * n/2 * (n/2)/2 = n³
    for starting_point in range(0, len(input_string)): # n
        for ending_point in range(starting_point+1, len(input_string)): # n-1, n-2, ... -> average: 1.5, n = 3; n/2
            print(f"\nstarting_point: {starting_point}, ending_point: {ending_point}")
            
            substring = input_string[starting_point:ending_point+1]
            if is_palindrome(substring): # no_operations_inner = (n/2)/2
                print(substring)
                list_of_strings.append(substring)
        # substring = input_string[0:ending_point+1]
        # ending_point += 1
    return list_of_strings

result = get_all_palidromes('abc') # 2, 3, 2; n=3    (2+3+2)/3 = 2.33
# n = 3
# The inner loop is called twice, and the total number of operation is 3.
# Average operation per loop call is 3/2 = 1.5.

# First run of the outer loop leads to 2x inner.
# Second run of the outer loop leads to 1x inner.

# Call loop 2 times
# 2 times + 1 times = 3 times
# average times of excution of the inner loop per call of the inner loop = 1.5
print(f"List of strings: {result}")