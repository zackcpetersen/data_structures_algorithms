class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '{} Next: {}'.format(self.value, self.next)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return 'First: {} Last: {} Length: {}'.format(self.first, self.last, self.length)

    def peek(self):
        print(self.first.value)
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if not self.length:
            self.first = new_node
        elif self.length == 1:
            self.first.next = new_node
        else:
            self.last.next = new_node

        self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.length:
            raise IndexError('Cannot dequeue an empty queue!')
        elif self.length == 1:
            self.last = None
            self.first = None
        else:
            old_fist = self.first
            self.first = self.first.next
            self.length -= 1
            return old_fist

    def is_empty(self):
        if self.length:
            print(False)
            return False
        print(True)
        return True

    def print_queue(self):
        print(self)


my_queue = Queue()
my_queue.enqueue('google')
my_queue.is_empty()
my_queue.enqueue('udemy')
my_queue.enqueue('youtube')
my_queue.dequeue()
my_queue.peek()

my_queue.print_queue()
