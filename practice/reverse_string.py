# Create a function that reverses a string
# 'Hello, My name is Zack!'
# !kcaZ si eman yM ,olleH'

my_str = 'Hello, My name is Zack!'


def reverse(my_str):
    if type(my_str) == str:
        my_list = list(my_str)
        new_str = ''
        backward = []
        for i in range(len(my_list)-1, -1, -1):
            backward.append(my_list[i])

        print(new_str.join(backward))
    else:
        print('Please input a string!')

def reverse2(my_str):
    my_list = list(my_str)
    my_list.reverse()
    my_str = ''

    print(my_str.join(my_list))


# reverse(my_str)
reverse2(my_str)