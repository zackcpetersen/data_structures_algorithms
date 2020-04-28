from trees.binary_search_tree import iterative_tree


def breadth_first_search_iterative(tree):
    current_node = tree.root
    array = []
    queue = [current_node]
    # queue.append(current_node)
    while len(queue):
        current_node = queue.pop(0)
        array.append(current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return array


def breadth_first_search_recursive(queue, list):
    if not len(queue):
        return list
    current_node = queue.pop(0)
    list.append(current_node.val)

    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)

    return breadth_first_search_recursive(queue, list)


breadth_first_result = [9, 4, 20, 1, 6, 15, 170, 25]
assert breadth_first_search_iterative(iterative_tree) == breadth_first_result
assert breadth_first_search_recursive([iterative_tree.root], []) == breadth_first_result
