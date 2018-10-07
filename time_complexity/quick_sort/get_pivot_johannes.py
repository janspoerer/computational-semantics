def get_pivot(list):
    low = list[0] 
    high = list[7]
    mid = (low + high - 1) // 2

    if mid <= low <= high: 
        pivot = low
        return pivot
        if low <= mid <= high: 
            pivot = mid
            return pivot
            if low <= high <= mid: 
                pivot = high
                return pivot
                if mid <= high <= low:
                    pivot = high
                    return pivot

list = [7, 5, 3, 2, 6, 8, 9, 1]
print(list)
get_pivot(list)
print(pivot)