class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '{} Next: {}'.format(self.value, self.next)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return 'Top: {} Bottom: {} Length: {}'.format(self.top, self.bottom, self.length)

    def peek(self):
        print(self.top.value)
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if not self.length:
            self.bottom = new_node
        elif self.length == 1:
            self.bottom.next = new_node
        else:
            self.top.next = new_node

        self.top = new_node
        self.length += 1

    def pop(self):
        if not self.length:
            return None
        if self.length == 1:
            self.bottom = None
        curr_node = self.bottom
        while curr_node.next is not self.top:
            curr_node = curr_node.next
        self.top = curr_node
        self.top.next = None
        self.length -= 1

    def is_empty(self):
        if self.length:
            print(False)
            return False
        print(True)
        return True

    def print_stack(self):
        print(self)


def call_functions():
    my_stack = Stack()
    my_stack.is_empty()
    my_stack.push('google')
    my_stack.push('udemy')
    my_stack.push('youtube')
    my_stack.pop()
    my_stack.peek()

    my_stack.print_stack()
