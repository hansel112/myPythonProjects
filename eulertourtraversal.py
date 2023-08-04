nodeChildren = {
    1: [2, 3],
    2: [4, 5],
    5: [8, 9],
    3: [6, 7]
}

elements = []
levels = []


def traverseNode(node, level=0):
    elements.append(node)
    levels.append(level)
    if node in nodeChildren:
        for child in nodeChildren[node]:
            traverseNode(child, level+1)
            elements.append(node)
            levels.append(level)


traverseNode(1)

print(f"node elements: {elements}")
# output: node elements: [1, 2, 4, 2, 5, 8, 5, 9, 5, 2, 1, 3, 6, 3, 7, 3, 1]

print(f"levels: {levels}")
# output: levels: [0, 1, 2, 1, 2, 3, 2, 3, 2, 1, 0, 1, 2, 1, 2, 1, 0]


