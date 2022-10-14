"""
Determine if a sequence of numbers is increasing
Given a sequence of numbers, determine if each element is larger than the previous element
"""
def is_ascending(list_of_numbers):
    # Optional: Argument checking (should all be numbers)
    sum(list_of_numbers) # n
    
    # Another argument check: List must at least have two elements
    if len(list_of_numbers) < 2:
        print("Problem. Number too small.")
        return None
    
    i = 0
    while i < (len(list_of_numbers) - 1): # n
        print(f"i: {i}")
        print(f"list_of_numbers: {list_of_numbers}")
        if list_of_numbers[i] >= list_of_numbers[i+1]:
            return False
        i += 1 # i = i + 1
    
    return True

is_ascending([1, 2, 2]) # -> False