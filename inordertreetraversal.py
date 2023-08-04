class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#                   1
#               2       3
#           4       5


def inorder(node):

    path = ''

    if node:
        path += inorder(node.left)
        path += (str(node.value) + "_")
        path += inorder(node.right)

    return path


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\n Inorder traversal of the tree is")


print(inorder(root))

# prints 4_2_5_ 1_ 3_
