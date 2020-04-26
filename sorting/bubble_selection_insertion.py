import copy

def bubble_sort(arr):
    length = len(arr)-1
    for i in range(length):
        for j in range(length):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if arr[j] < arr[i] and j >= i:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            temp = arr[i]
            arr.remove(temp)
            arr.insert(0, temp)
        elif arr[i] > arr[i-1]:
            pass
        else:
            for j in range(i):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr.remove(temp)
                    arr.insert(j, temp)
    return arr


sorted_arr = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
unsorted_arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

array = copy.copy(unsorted_arr)
assert bubble_sort(array) == sorted_arr
array = copy.copy(unsorted_arr)
assert selection_sort(array) == sorted_arr
array = copy.copy(unsorted_arr)
assert insertion_sort(array) == sorted_arr
