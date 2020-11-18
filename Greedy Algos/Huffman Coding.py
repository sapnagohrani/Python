string = 'BCAADDDCCACACAC'  # String needs to be converted in huffman code


# Converting frequency dequeue to tree
class Tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, bin_string + '0'))
    d.update(huffman_code_tree(r, bin_string + '1'))
    return d


# Calculating frequency of each character in String
freq = {}  # Empty dictionary containg character of string as a key & frequency as a value
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
# Converting Freq dictionary into a list ordered by frequency
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(freq)
# from sorted queue pop 2 items make a node of tree and assign sum of frequency of popped items to queue
nodes = freq
while len(nodes) > 1:
    (k1, c1) = nodes[-1]
    (k2, c2) = nodes[-2]
    node = Tree(k1, k2)
    nodes = nodes[:-2]
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
# Calling Huffman Function
huffman_code = huffman_code_tree(nodes[0][0])
print(huffman_code)
