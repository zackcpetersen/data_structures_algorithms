nemo = ['nemo']


def find_nemo(arr):
    for i in arr:
        if i == 'nemo':
            print('Found NEMO!')


# find_nemo(nemo)  # O(n) --> linear time


def log_fist_to_boxes(boxes):
    print(boxes[0])  # O(1)
    print(boxes[1])  # O(2)


boxes = [0, 1, 2, 3, 4, 5]
# log_fist_to_boxes(boxes)  # O(1) --> constant time

def funChallenge(input):
    # not meant to be run - just to demonstrate big O
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in input:  # O(n)
        another_function()  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)

    return a  # O(1)
    # O(3 + 4n)


def log_arr_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# log_arr_pairs(boxes)  # O(n^2) --> quadratic time


# SPACE COMPLEXITY
def boo(n):
    for i in range(n):
        print('boo')


# boo(5)  # space complexity O(1)


def fill_arr(n):
    hi_arr = [None] * n
    for i in range(n):
        hi_arr[i] = 'hi'
    print(hi_arr)


# fill_arr(10)  # O(n)
