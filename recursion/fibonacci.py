def fibonacci_recursive(num):
    if num <= 2:
        return 1
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


def fibonacci_iterative(num):
    result = 1
    prev = 1
    index = 3
    while num >= index:
        temp = result
        result += prev
        prev = temp
        index += 1
    return result


def fibonacci_iterative_two(num):
    sequence = [0, 1]
    for i in range(2, num+1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[num]


assert fibonacci_recursive(10) == 55
assert fibonacci_iterative(10) == 55
assert fibonacci_iterative_two(10) == 55
