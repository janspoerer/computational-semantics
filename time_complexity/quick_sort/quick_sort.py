import random
import time
import matplotlib.pyplot as plt
from tkinter import *

def find_pivot_index(list):
    """
    Finds the median of the first 3 elements in a list
    """
    low = 0
    high = -1
    mid = len(list) // 2

    if (list[mid] <= list[low] <= list[high]):
        result = low
    elif (list[high] <= list[low] <= list[mid]):
        result = low
    elif (list[low] <= list[mid] <= list[high]):
        result = mid
    elif (list[high] <= list[mid] <= list[low]):
        result = mid
    elif (list[low] <= list[high] <= list[mid]):
        result = high
    elif (list[mid] <= list[high] <= list[low]):
        result = high

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

    result = []
    result.extend(left)
    result.append(list[border_index]) # The pivot value will be at this index because we earlier swapped the border and the pivot
    result.extend(right)

    return result

results_best = []
results_base = []
results_worst = []
decksizes = [10, 100, 1000]
repetition_limit = 50

# Best case (already sorted)
for n in range(0, len(decksizes)):
    sum = 0
    for repetition in range( 1, repetition_limit ):
        state = list(range( 1, decksizes[n] ))
        state.sort()
        start = time.time()
        quick_sort(state)
        sum = sum + ( time.time() - start )
    average = sum / repetition_limit
    print(sum)
    results_best.append ( average )

# Base case (random)
for n in range(0, len(decksizes)):
    sum = 0
    for repetition in range( 1, repetition_limit ):
        state = list(range( 1, decksizes[n] ))
        random.shuffle( state )
        start = time.time()
        quick_sort(state)
        sum = sum + ( time.time() - start )
    average = sum / repetition_limit
    print(sum)
    results_base.append ( average )

# Worst case (reverse sorted, descending)
for n in range(0, len(decksizes)):
    sum = 0
    for repetition in range( 1, repetition_limit ):
        state = list(range( 1, decksizes[n] ))
        state.sort(reverse=True)

        # Causing some bad pivots
        state[0]
        state[1]
        state[2]
        state[3]
        state[len(state) // 2]
        state[(len(state) // 2) + 1]
        state[(len(state) // 2) + 2]
        state[(len(state) // 2) + 3]

        start = time.time()
        quick_sort(state)
        sum = sum + ( time.time() - start )
    average = sum / repetition_limit
    print(sum)
    results_worst.append ( average )

print(results_best)
x = decksizes
# create an index for each tick position
xi = [i for i in range(0, len(x))]
plt.plot(xi, results_best, color="green")
plt.plot(xi, results_base, color="orange")
plt.plot(xi, results_worst, color="red")
# plt.xticks([1, 2, 3, 4])
plt.ylabel("time complexity")
plt.xlabel("length of list")
plt.xticks(xi, x)
plt.title('Compare best, base, and worst cases')
plt.show()
