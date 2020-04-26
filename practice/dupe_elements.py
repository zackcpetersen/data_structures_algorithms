arr1 = ['a', 'b', 'x', 'f']
arr2 = ['z', 'y', 'd']

'find duplicate elements in each array'
'will input always be integers? strings?'
'what is main goal? speed?'


def find_dupes(arr1, arr2):
    arr1_dict = {element: True for element in arr1}

    for ele in arr2:
        if arr1_dict.get(ele):
            return True, arr1_dict.get(ele)


# print(find_dupes(arr1, arr2))

# arr1.index(arr2['a'])
print('g' in arr1)