def reverse_string(string):
    arr_str = list(string)
    reversed = []

    def add_to_arr(arr):
        if len(arr) > 0:
            reversed.append(arr.pop())
            add_to_arr(arr)

    add_to_arr(arr_str)
    return ''.join(reversed)


assert reverse_string('hello world') == 'dlrow olleh'
