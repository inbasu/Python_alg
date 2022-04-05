from collections import Counter


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def get_code(node, bins=''):
    if node is None:
        return 
    if type(node) is str:
        return {node: bins}
    code={}
    code.update(get_code(node.left, bins + '0'))
    code.update(get_code(node.right, bins + '1'))
    return code


def hu_tree(string):
    nodes = Counter(string).most_common()
    if len(nodes) <= 1:
        node = Node(None)
        if len(nodes) == 1:
            node.left = Node(nodes[0][0])
            node.right = None
        nodes = [(node, 1)]
        print(nodes)
    while len(nodes) > 1:
        key1, val1 = nodes[-1]
        key2, val2 = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1, key2)
        nodes.append((node, val1 + val2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    print(nodes)
    return get_code(nodes[0][0])


def huffman(text):
    tree = hu_tree(text)
    result = ''
    for ch in text:
        result += tree[ch] + ' '
    return result


if __name__ == '__main__':
    text = 'lorem ipsum dolor sit amet'
    print(huffman(text))
