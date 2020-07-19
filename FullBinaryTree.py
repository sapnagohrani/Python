class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


# Full Binary Tree Logic -> all the nodes must have 0 or 2 nodes
def is_full_binary(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full_binary(root.left) and is_full_binary(root.right)
    return False


root1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
root2 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))

print('Tree 1', end=' ')
if is_full_binary(root1):
    print('is a full binary tree')
else:
    print('is not a full binary tree')

print('Tree 2', end=' ')
if is_full_binary(root2):
    print('is a full binary tree')
else:
    print('is not a full binary tree')
