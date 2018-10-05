def quick_sort(list):
    # We could consider to allow for flexible pivot indexes
    print("input", list)
    if len(list) < 1:
        return []

    border_offset = 1
    border_index = 0

    while (border_index + border_offset + 1) < (len(list)):
        border_index = border_index + 1
        if list[border_index + border_offset] < list[0]:
            # Swap border and compared value
            temporary_value = list[border_index]
            list[border_index] = list[border_index + border_offset]
            list[border_index + border_offset] = temporary_value

            #
            border_offset = 1
        else:
            border_offset = border_offset + 1

    # Swap border and pivot
    temporary_value = list[border_index]
    list[border_index] = list[0]
    list[0] = temporary_value

    print("after", list)

    left = []
    # Recursively call the function for the left side
    left = quick_sort(list[0:border_index])
    right = []
    # Recursively call the function for the right side
    right = quick_sort(list[border_index:])

    result = []
    result.extend[left]
    result.extend[right]
    return result

list = [7, 5, 3, 2, 6, 8, 9, 1]
quick_sort(list)
