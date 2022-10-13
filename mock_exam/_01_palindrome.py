"""
Determine if a given string is a palindrome
A palindrome is sequence that reads same backwards as forwards. 

“Anna”, for example is a palindrome.

The task is to determine if a given string is a palindrome
"""
def is_palindrome(given_string) -> bool:
    given_string = given_string.lower()
    
    reverse_word = ""
    for position in range(0, len(given_string)):
        position = position + 1
        reverse_word = reverse_word + given_string[-position]

    if reverse_word == given_string:
        return True
    else:
        return False


        

assert(is_palindrome("Anna"))

assert(is_palindrome("Ana"))

assert(not is_palindrome("Jan"))

