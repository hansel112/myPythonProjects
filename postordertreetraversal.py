class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#                   1
#               2       3
#           4       5


def postorder(node):

    path = ''

    if node:
        path += postorder(node.left)
        path += postorder(node.right)
        path += (str(node.value) + "_")

    return path


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\n Postorder traversal of the tree is ")


print(postorder(root))

# prints 4_5_2_ 3_ 1_
