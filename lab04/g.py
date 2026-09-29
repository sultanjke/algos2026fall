class Node:
    def __init__(self, value, order):
        self.value = value
        self.order = order
        self.left = None
        self.right = None
        self.height = 1


def build_tree(values):
    nodes = []
    seen = set()

    for value in values:
        if value not in seen:
            nodes.append(Node(value, len(nodes)))
            seen.add(value)

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
nodes = [root]

for node in nodes:
    if node.left is not None:
        nodes.append(node.left)
    if node.right is not None:
        nodes.append(node.right)

diameter = 0

for node in reversed(nodes):
    left_height = 0
    right_height = 0

    if node.left is not None:
        left_height = node.left.height
    if node.right is not None:
        right_height = node.right.height

    node.height = max(left_height, right_height) + 1
    diameter = max(diameter, left_height + right_height + 1)

print(diameter)
