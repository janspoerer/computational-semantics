def find_pivot_index(list):
    """
    Finds the median of the first 3 elements in a list
    """
    if ((list[0] < list[1]) and (list[1] < list[2])) or ((list[2] < list[1]) and (list[1] < list[0])):
        return 1
    if ((list[1] < list[0]) and (list[0] < list[2])) or ((list[2] < list[0]) and (list[0] < list[1])):
        return 0
    if ((list[0] < list[2]) and (list[2] < list[1])) or ((list[1] < list[2]) and (list[2] < list[0])):
        return 2

def swap(list, first_index, second_index):
    temporary_value = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = temporary_value
    return list

def quick_sort(list):
    print("input", list)

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

    print(list[pivot_index])

    # Swap pivot to first position
    list = swap(list, pivot_index, 0)

    border_offset = 1
    border_index = 1

    while (border_index + border_offset) < (len(list)):
        # print("border_index: ", border_index, "; border_offset: ", border_offset, "; 1")
        # print(list)
        if list[border_index + border_offset] < list[0]:
            # Swap border and compared value
            list = swap(list, border_index, border_index + border_offset)

            if (border_index + border_offset + 1) < (len(list)):
                border_index = border_index + 1
            else:
                break
        else:
            border_offset = border_offset + 1
        # print("border_index: ", border_index, "; border_offset: ", border_offset, "; 1")
        print("Iteration: ", list)
    print(list)
    if list[-1] < list[border_index]:
        list = swap(list, -1, border_index + 1)
        border_index = border_index + 1
    print("After swap: ", list)

    # Swap border and pivot
    list = swap(list, border_index, 0)

    print("components", list[0:border_index], list[border_index], list[border_index + 1:])

    left = []
    # Recursively call the function for the left side
    # Skip the recursive call if there is only one element left
    if len(list[0:border_index]) == 1:
        left = list[0:border_index]
    else:
        left = quick_sort(list[0:border_index])
    print("output left", left)

    right = []
    # Recursively call the function for the right side
    # Skip the recursive call if there is only one element left
    if len(list[border_index + 1:]) == 1:
        right = list[border_index + 1:]
    else:
        right = quick_sort(list[border_index + 1:])
    print("output right", right)

    result = []
    result.extend(left)
    result.append(list[border_index]) # The pivot value will be at this index because we earlier swapped the border and the pivot
    result.extend(right)
    print("RESULT!!!!!: ", result)
    return result

list = [7, 5, 3, 2, 6, 8, 9, 1]
print("END RESULT", quick_sort(list))
