# 1 --> 10 --> 5 --> 16
# Simple linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return 'Value: {} Next: {}'.format(self.value, self.next.value)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return 'head: {}\ntail: {}\nlength: {}'.format(self.head, self.tail, self.length)

    def print_list(self):
        list_arr = []
        current_node = self.head
        while current_node is not None:
            list_arr.append(current_node.value)
            current_node = current_node.next
        print(list_arr, self.length)

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def traverse_to_index(self, index):
        i = 0
        current_node = self.head
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif self.length >= index:
            new_node = Node(value)
            leader = self.traverse_to_index(index - 1)
            follower = leader.next
            leader.next = new_node
            new_node.previous = leader
            new_node.next = follower
            if follower:
                follower.previous = new_node
            else:
                self.tail = new_node
            self.length += 1
        else:
            raise AttributeError('List index out of range')

    def remove(self, index):
        if self.length <= index or index < 0:
            raise AttributeError('List index out of range')
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return self
        else:
            leader = self.traverse_to_index(index - 1)
            follower = leader.next
            if follower.next:
                follower.next.previous = follower
            leader.next = follower.next
            if follower.next is None:
                self.tail = leader
            if leader.next:
                leader.next.previous = leader
            self.length -= 1

    def reverse_doubly(self):
        i = 0
        current_node = self.tail
        reversed_list = []
        while i < self.length:
            print(i)
            reversed_list.append(current_node.value)
            current_node = current_node.previous
            i += 1
        print(reversed_list)
        return reversed_list

    def reverse_singly(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return self


my_list = LinkedList(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.prepend(1)
my_list.insert(4, 69)
my_list.remove(4)
# my_list.reverse_doubly()
my_list.reverse_singly()

my_list.print_list()
