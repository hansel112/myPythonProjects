from queue import Queue
tree = {'A': ['B', 'C', 'E'], 'B': ['D'], 'C': ['F', 'G'], 'E': [], 'D': [], 'F': [], 'G': []}


def bfs(input_tree, source):
    Q = Queue()
    visited_nodes = list()
    Q.put(source)
    visited_nodes.append(source)
    while not Q.empty():
        node = Q.get()
        print(node, end=" ")
        for u in input_tree[node]:
            if u not in visited_nodes:
                Q.put(u)
                visited_nodes.append(u)


print("BFS tree traversal with root A is:")
bfs(tree, "A")
