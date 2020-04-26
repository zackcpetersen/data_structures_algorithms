array_1 = [9, 3, 5, 8]
array_2 = [24, 33, 0]


# This should probably have another function that does sorting manually
def merge_sorted_arrays(arr1, arr2):
    arr1.extend(arr2)
    sorted_arr = sorted(arr1)
    print(sorted_arr)


merge_sorted_arrays(array_1, array_2)
