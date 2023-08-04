from graphviz import Digraph

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def draw_tree(node, dot=None):
    if dot is None:
        dot = Digraph()
        dot.node(str(node.value), str(node.value))
    if node.left is not None:
        dot.node(str(node.left.value), str(node.left.value))
        dot.edge(str(node.value), str(node.left.value))
        draw_tree(node.left, dot)
    if node.right is not None:
        dot.node(str(node.right.value), str(node.right.value))
        dot.edge(str(node.value), str(node.right.value))
        draw_tree(node.right, dot)
    return dot

# Define the binary tree
tree = Node(47)
tree.left = Node(36)
tree.right = Node(66)

tree.left.left = Node(25)
tree.left.right = Node(39)
tree.left.right.left = Node(38)
tree.left.right.right = Node(42)

tree.right.left = Node(63)
tree.right.left.right = Node(64)
tree.right.right = Node(68)

# Usage:
dot = draw_tree(tree)
dot.render('tree.png', format='png')