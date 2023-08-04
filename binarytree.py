from anytree import Node, RenderTree

# Define the nodes of the tree
root = Node(47)
node36 = Node(36, parent=root)
node66 = Node(66, parent=root)
node25 = Node(25, parent=node36)
node39 = Node(39, parent=node36)
node38 = Node(38, parent=node39)
node42 = Node(42, parent=node39)
node63 = Node(63, parent=node66)
node64 = Node(64, parent=node63)
node68 = Node(68, parent=node66)

# Usage:
for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
