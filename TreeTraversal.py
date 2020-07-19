class TreeTraversal:
    def __init__(self, info, left=None, right=None):
        self.value = info
        self.left = left
        self.right = right


def in_order(root):
    if root:
        in_order(root.left)
        print(str(root.value) + '->', end='')
        in_order(root.right)


def pre_order(root):
    if root:
        print(str(root.value) + '->', end='')
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(str(root.value) + '->', end='')


tree_left = TreeTraversal(2, TreeTraversal(4), TreeTraversal(5))
tree_right = TreeTraversal(3, TreeTraversal(6), TreeTraversal(7))
root = TreeTraversal(1, tree_left, tree_right)

in_order(root)
print('InOrder - Traversal')

pre_order(root)
print('PreOrder - Traversal')

post_order(root)
print('PostOrder - Traversal')



