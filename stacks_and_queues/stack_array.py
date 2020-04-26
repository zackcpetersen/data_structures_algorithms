class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)


class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return 'Data: {} Length: {}'.format(self.data, len(self.data))

    def peek(self):
        return self.data[-1]

    def push(self, value):
        new_node = Node(value)
        self.data.append(new_node)
        return self

    def pop(self):
        if len(self.data):
            del self.data[-1]
            return self
        raise IndexError('Cannot pop empty stack')


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')

my_stack.pop()
my_stack.peek()
print(my_stack)
