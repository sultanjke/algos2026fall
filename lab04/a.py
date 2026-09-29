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

    nodes.sort(key=lambda node: (node.value, -node.order))
    stack = []

    for node in nodes:
        while stack and stack[-1].order > node.order:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)

    return stack[0]


input = open(0).readline
n, m = map(int, input().split())
values = list(map(int, input().split()))
root = build_tree(values)
answers = []

for path_number in range(m):
    path = input().strip()
    current = root

    for direction in path:
        if current is None:
            break
        if direction == "L":
            current = current.left
        else:
            current = current.right

    if current is None:
        answers.append("NO")
    else:
        answers.append("YES")

print("\n".join(answers))
