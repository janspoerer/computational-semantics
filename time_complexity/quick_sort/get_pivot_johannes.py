def get_pivot(list):
    low = 0
    high = -1
    mid = len(list) // 2

    print(low, list[low])
    print(mid, list[mid])
    print(high, list[high])

    if (list[mid] <= list[low] <= list[high]):
        result = low
    if (list[high] <= list[low] <= list[mid]):
        result = low
    if (list[low] <= list[mid] <= list[high]):
        result = mid
    if (list[high] <= list[mid] <= list[low]):
        result = mid
    if (list[low] <= list[high] <= list[mid]):
        result = high
    if (list[mid] <= list[high] <= list[low]):
        result = high

    return result

#list = [8, 6, 5, 1, 3, 2, 9, 7]
list = [7, 5, 3, 2, 6, 8, 9, 1]
print(list)
print(get_pivot(list))
