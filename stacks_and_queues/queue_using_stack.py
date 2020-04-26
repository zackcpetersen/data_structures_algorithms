from stack_linked_list import Stack


class Queue:
    def __init__(self):
        self.data = Stack()

    def __str__(self):
        return '{}'.format(self.data)

    def peek(self):
        print(self.data.bottom.value)
        return self.data.bottom.value

    def push(self, value):
        self.data.push(value)
        # print(self.data)
        return self.data

    def pop(self):
        if not self.data.length:
            return None
        if self.data.length == 1:
            self.data.top = None
        bottom = self.data.bottom
        self.data.bottom = self.data.bottom.next
        self.data.length -= 1
        print(self.data)
        return bottom

    def is_empty(self):
        return False if self.data.length else True


def call_functions():
    # use python -i queue_using_stack.py to call this function
    my_queue = Queue()
    print(my_queue.is_empty())
    my_queue.push('zackcpetersen.com')
    my_queue.push('youtube.com')
    my_queue.push('stackoverflow.com')
    my_queue.pop()
    my_queue.peek()
