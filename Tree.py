class Tree:
    def __init__(self, info, left_child=None, right_child=None):
        self.info = info
        self.left = left_child
        self.right = right_child

    def __str__(self):
        return str(str(self.info) + ' Has Left Child : ' + str(self.left) + ' & Right Child : ' + str(self.right))


tree = Tree(1, Tree(2, 3, 4), Tree(5, 6, 7))

print(tree)
