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

level = [root]
sums = []

while level:
    total = 0
    next_level = []

    for node in level:
        total += node.value
        if node.left is not None:
            next_level.append(node.left)
        if node.right is not None:
            next_level.append(node.right)

    sums.append(total)
    level = next_level

print(len(sums))
print(*sums)
