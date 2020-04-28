import math


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    middle = length // 2
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    print(left, right)
    return result + left[l_index:] + right[r_index:]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283]
arr_sorted = merge_sort(numbers)
print(arr_sorted)
