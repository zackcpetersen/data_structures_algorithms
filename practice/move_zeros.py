# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
array = [0, 1, 0, 3, 12]


def move_zeros(arr):
    for i, item in enumerate(arr):
        if item == 0:
            del(arr[i])
            arr.append(0)
    print(arr)


move_zeros(array)
