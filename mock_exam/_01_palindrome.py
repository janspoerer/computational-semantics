"""
Determine if a given string is a palindrome
A palindrome is sequence that reads same backwards as forwards. 

“Anna”, for example is a palindrome.
-> Ana
-> abc cba
-> Note that we have a capital A 

The task is to determine if a given string is a palindrome
"""
def is_palindrome(input_string):
    # Idea 3
    # Access the first element with a 0.
    # Last element with length - 1.
    # Loop that compares first with last, second with penultimate, and so on ...
    # Ignore the middle letter if we have an oddly-numbered word.
    # Time complexity?
    # -> .lower()
    # -> rest will be O(n/2)

    # Should we do .lower() for the whole string? Or on the fly (in the loop)?
    # If we do .lower() on a lower-case string, we still have to check the 
    # capitalization of EACH character!

    # input_string = abc  -> odd will ignore middle character
    # input_string = abbc -> even will check middle characters

    first_index = 0
    # last_index = len(input_string) - 1
    while first_index < len(input_string) // 2:
        # if input_string[first_index] == input_string[len(input_string) - first_index - 1]:
        if input_string[first_index].lower() == input_string[-(first_index + 1)].lower():
            first_index += 1
        else:
            return False

    return True

if is_palindrome("ABCC CCCA"):
    print("True")
else: 
    print("False") # -> This one

if is_palindrome("Anna"):
    print("True") # -> This one
else:
    print("False")

if is_palindrome("Ana"):
    print("True") # -> This one
else:
    print("False")

if not is_palindrome("Jan"):
    print("True")
else:
    print("False") # -> This one





































