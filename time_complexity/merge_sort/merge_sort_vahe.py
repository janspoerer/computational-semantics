def merge_sort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    print("left side: ", left)
    print("right side: ", right)
    merged_list = reduce(left, right)
    print("merged: ", merged_list)
    return merged_list


def reduce(left, right):
    if len(left) == 0 or len(right) == 0:
        return []

    result = []
    left_index = 0
    right_index = 0
    final_length = len(left) + len(right)

    while (len(result) < final_length):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        if left_index == len(left):
            result.extend(right[right_index:])
            break
        if right_index == len(right):
            result.extend(left[left_index:])
            break

    return result

data = [4, 9, 6, 5, 2, 3, 1, 7, 8]
merge_sort(data)
