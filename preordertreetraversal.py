
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#                   1
#               2       3
#           4       5


def preorder(node):

    path = ''

    if node:
        path += (str(node.value) + "_")
        path += preorder(node.left)
        path += preorder(node.right)

    return path


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\n Preorder traversal of the tree is")


print(preorder(root))

# prints 1_2_4_ 5_  3_
