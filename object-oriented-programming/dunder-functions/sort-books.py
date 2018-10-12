import random
import time
import matplotlib.pyplot as plt
from tkinter import *
import books

def find_pivot_index(list):
    """
    Finds the median of the first 3 elements in a list
    """
    low = 0
    high = -1
    mid = len(list) // 2

    if (list[mid] <= list[low] <= list[high]):
        result = low

    return result

def swap(list, first_index, second_index):
    """
    Swaps two elements in a list
    """
    temporary_value = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = temporary_value
    return list

def quick_sort(list):
    """
    Sorts a list of numbers in ascending order
    """

    # No border sorting needed if there are less than 3 elements
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list
    if len(list) == 2:
        result = []
        if list[0] < list[1]:
            result.append(list[0])
            result.append(list[1])
        else:
            result.append(list[1])
            result.append(list[0])
        return result

    pivot_index = find_pivot_index(list)

    # Swap pivot to first position
    list = swap(list, pivot_index, 0)

    border_offset = 1
    border_index = 1

    while (border_index + border_offset) < (len(list)):
        if list[border_index + border_offset] <= list[0]:
            # Swap border and compared value
            list = swap(list, border_index, border_index + border_offset)
            border_offset = 1
            border_index = border_index + 1
        else:
            border_offset = border_offset + 1

    # Check if last value is smaller than the pivot and swap if necessary
    if (list[-1] <= list[0]) and (border_index + 1 < len(list)):
        swap(list, border_index + 1, -1)
        border_index = border_index + 1

    # Check if border is larger than pivot and exclude it from the left list if yes
    if list[border_index] > list[0]:
        border_index = border_index - 1

    # Swap border and pivot
    list = swap(list, border_index, 0)

    left = []
    # Recursively call the function for the left side
    # Skip the recursive call if there is only one element left
    if len(list[0:border_index]) == 1:
        left = list[0:border_index]
    else:
        left = quick_sort(list[0:border_index])

    right = []
    # Recursively call the function for the right side
    # Skip the recursive call if there is only one element left
    if len(list[border_index + 1:]) == 1:
        right = list[border_index + 1:]
    else:
        right = quick_sort(list[border_index + 1:])

    print("left************************************")
    for item in left:

        print(item)

    print("mid", str(list[pivot_index]))

    print("right************************************")
    for item in right:

        print(item)

    result = []
    result.extend(left)
    result.append(list[border_index]) # The pivot value will be at this index because we earlier swapped the border and the pivot
    result.extend(right)

    return result

all_books = []
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 102))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 103))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 104))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 105))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 106))
all_books.append(books.Book("Name 1", "Author 1", "isbn 1", 1))
all_books.append(books.Book("Name 2", "Author 2", "isbn 2", 2))
all_books.append(books.Book("Name 4", "Author 4", "isbn 4", 4))
all_books.append(books.Book("Name 5", "Author 5", "isbn 5", 5))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 3))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 100))
all_books.append(books.Book("Name 3", "Author 3", "isbn 3", 101))

print("BEFORE")
for book in all_books:
    print(book)

sorted_list_all_books = quick_sort(all_books)

print("After")
for book in sorted_list_all_books:
    print(book)
