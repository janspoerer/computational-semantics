def get_pivot(list):
    low = list[0]
    high = list[-1]
    mid = list[len(list) // 2]

    print(low)
    print(mid)
    print(high)

    if (mid <= low <= high):
        result = low
    if (high <= low <= mid):
        result = low
    if (low <= mid <= high):
        result = mid
    if (high <= mid <= low):
        result = mid
    if (low <= high <= mid):
        result = high
    if (mid <= high <= low):
        result = high

    return result

#list = [8, 6, 5, 1, 3, 2, 9, 7]
list = [7, 5, 3, 2, 6, 8, 9, 1]
print(list)
print(get_pivot(list))