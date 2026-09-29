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

stack = []
current = root
total = 0
answer = []

while current is not None or stack:
    while current is not None:
        stack.append(current)
        current = current.right

    current = stack.pop()
    total += current.value
    current.value = total
    answer.append(current.value)
    current = current.left

print(*answer)
