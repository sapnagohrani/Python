class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(str(node.info) + '->', end='')
        in_order_traversal(node.right)


def insert(node, key):
    if node is None:
        return Tree(key)
    if key < node.info:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def get_min_value_node(node):
    while node.left is not None:
        node = node.left
    return node


def delete_node(node, key):
    if node is None:
        return node
    if key < node.info:
        node.left = delete_node(node.left, key)
    elif key > node.info:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            return temp
        elif node.right is None:
            temp = node.left
            return temp
        temp = get_min_value_node(node.right)
        node.info = temp.info
        node.right = delete_node(node.right, temp.info)
    return node


root = Tree(50, Tree(30, Tree(20), Tree(40)), Tree(70, Tree(60), Tree(80)))  # Tree is BST
root = insert(root, 100)
root = insert(root, 10)
root = insert(root, 45)
in_order_traversal(root)
delete_node(root, 60)
print('After deletion : ')
in_order_traversal(root)
