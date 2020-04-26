class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return '{}'.format(self.val)


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return '{}'.format(self.root)

    def insert(self, val):
        raise NotImplementedError()

    def lookup(self, val):
        raise NotImplementedError()


class BinaryTreeRecursive(Tree):
    def insert(self, val, node=None):
        if not self.root:
            self.root = Node(val)
            return self.root
        curr_node = node if node else self.root
        if val > curr_node.val:
            if curr_node.right:
                self.insert(val, curr_node.right)
                return self.root
            curr_node.right = Node(val)
            return self.root
        if curr_node.left:
            self.insert(val, curr_node.left)
            return self.root
        curr_node.left = Node(val)
        return self.root

    def lookup(self, val, node=None):
        if self.root:
            curr_node = node if node else self.root
            if val == curr_node.val:
                return curr_node
            if val > curr_node.val:
                if curr_node.right:
                    self.lookup(val, curr_node.right)
                    return self.root
                return False
            if curr_node.left:
                self.lookup(val, curr_node.left)
                return self.root
            return False
        return False


class BinaryTreeIterative(Tree):
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return self.root
        curr_node = self.root
        while True:
            if val > curr_node.val:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(val)
                    return self.root
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(val)
                    return self.root

    def lookup(self, val, save_pre=False):
        if self.root:
            curr_node = self.root
            while True:
                if val == curr_node.val:
                    return curr_node
                if val > curr_node.val:
                    if curr_node.right:
                        curr_node = curr_node.right
                    else:
                        return False
                else:
                    if curr_node.left:
                        curr_node = curr_node.left
                    else:
                        return False
        return False

    def remove(self, val):
        if self.root is None:
            return False

        curr_node = self.root
        parent_node = None
        while curr_node:
            if val < curr_node.val:
                parent_node = curr_node
                curr_node = curr_node.left
            elif val > curr_node.val:
                parent_node = curr_node
                curr_node = curr_node.right
            elif val == curr_node.val:
                if curr_node.right is None:
                    if parent_node is None:
                        self.root = curr_node.left
                    else:
                        if curr_node.val < parent_node.val:
                            parent_node.left = curr_node.left
                        elif curr_node.val > parent_node.val:
                            parent_node.right = curr_node.left
                elif curr_node.right.left is None:
                    curr_node.right.left = curr_node.left
                    if parent_node is None:
                        self.root = curr_node.right
                    else:
                        if curr_node.val < parent_node.val:
                            parent_node.left = curr_node.right
                        elif curr_node.val > parent_node.val:
                            parent_node.right = curr_node.right
                else:
                    leftmost = curr_node.right.left
                    leftmost_parent = curr_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    leftmost_parent.left = leftmost.right
                    leftmost.left = curr_node.left
                    leftmost.right = curr_node.right
                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if curr_node.val < parent_node.val:
                            parent_node.left = leftmost
                        elif curr_node.val > parent_node.val:
                            parent_node.right = leftmost
                return True


def traverse(node):
    tree = Node(node.val)
    tree.left = None if node.left is None else traverse(node.left)
    tree.right = None if node.right is None else traverse(node.right)
    print(tree)
    return tree


iterative_tree = BinaryTreeIterative()
iterative_tree.insert(9)
iterative_tree.insert(4)
iterative_tree.insert(6)
iterative_tree.insert(1)
iterative_tree.insert(20)
iterative_tree.insert(170)
iterative_tree.insert(15)
iterative_tree.insert(25)
iterative_tree.remove(20)

traverse(iterative_tree.root)
