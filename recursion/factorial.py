def factorial_recursive(num):
    if num == 1:
        return num
    return num * factorial_recursive(num-1)


def factorial_iterative(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


assert factorial_recursive(5) == 120
assert factorial_iterative(5) == 120
