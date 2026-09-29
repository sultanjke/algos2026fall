class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(value)
                break
            current = current.right

    return root


n = int(input())
values = list(map(int, input().split()))
root = None

for value in values:
    root = insert(root, value)

stack = [root]
leaves = 0

while stack:
    node = stack.pop()
    if node.left is None and node.right is None:
        leaves += 1
    if node.left is not None:
        stack.append(node.left)
    if node.right is not None:
        stack.append(node.right)

print(leaves)
