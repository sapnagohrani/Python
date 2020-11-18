class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


def calculate_depth(root):
    d = 0
    while root is not None:
        d += 1
        root = root.left
    return d


def is_full_binary(root, d, level=0):
    if root is None:
        return True
    # Logic - All nodes should have 0 or 2 children nodes
    if root.left is None and root.right is None:
        return d == level + 1
    # Logic - All leaf nodes are at same level
    if root.left is None or root.right is None:
        return False

    if root.left is not None and root.right is not None:
        return is_full_binary(root.left, d, level + 1) and is_full_binary(root.right, d, level + 1)


root1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
root2 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3))

print('Tree 1', end=' ')
if is_full_binary(root1, calculate_depth(root1)):
    print('is a perfect binary tree')
else:
    print('is not a perfect binary tree')

print('Tree 2', end=' ')
if is_full_binary(root2, calculate_depth(root2)):
    print('is a perfect binary tree')
else:
    print('is not a perfect binary tree')
