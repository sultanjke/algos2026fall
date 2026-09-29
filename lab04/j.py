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


n, k = map(int, input().split())
values = list(map(int, input().split()))

if k > n:
    print(-1)
else:
    root = build_tree(values)
    stack = []
    current = root
    count = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            print(current.value)
            break

        current = current.right
