from trees.binary_search_tree import iterative_tree


def depth_first_search_in_order(node, arr):
    if node.left:
        depth_first_search_in_order(node.left, arr)
    arr.append(node.val)

    if node.right:
        depth_first_search_in_order(node.right, arr)

    return arr


def depth_first_search_post_order(node, arr):
    if node.left:
        depth_first_search_post_order(node.left, arr)

    if node.right:
        depth_first_search_post_order(node.right, arr)

    arr.append(node.val)

    return arr


def depth_first_search_pre_order(node, arr):
    arr.append(node.val)

    if node.left:
        depth_first_search_pre_order(node.left, arr)

    if node.right:
        depth_first_search_pre_order(node.right, arr)

    return arr


print(depth_first_search_in_order(iterative_tree.root, []))
print(depth_first_search_post_order(iterative_tree.root, []))
print(depth_first_search_pre_order(iterative_tree.root, []))
