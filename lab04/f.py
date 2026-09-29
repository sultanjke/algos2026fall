class Node:
    def __init__(self, value, order):
        self.value = value
        self.order = order
        self.left = None
        self.right = None


def build_tree(values):
    nodes = []
    for order in range(len(values)):
        nodes.append(Node(values[order], order))

    nodes.sort(key=lambda node: node.value)
    stack = []

    for node in nodes:
        while stack and stack[-1].order > node.order:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)

    return stack[0]


n = int(input())
values = list(map(int, input().split()))
root = build_tree(values)
stack = [root]
triangles = 0

while stack:
    node = stack.pop()
    if node.left is not None and node.right is not None:
        triangles += 1
    if node.left is not None:
        stack.append(node.left)
    if node.right is not None:
        stack.append(node.right)

print(triangles)
