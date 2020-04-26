# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

# Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2


def first_recurring_char(inp):
    # uses 'in' to check an array
    new_arr = []
    for item in inp:
        if item in new_arr:
            print(item)
            return item
        new_arr.append(item)
    print(None)
    return None


def first_recurring_char_hash(inp):
    # uses dictionary (hash table) to find duplicates
    my_dict = {}
    for item in inp:
        if my_dict.get(item):
            print(item)
            return item
        my_dict.update({item: True})
    print(None)
    return None


array_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
array_4 = [2, 5, 5, 2, 3, 5, 1, 2, 4]

first_recurring_char_hash(array_1)
