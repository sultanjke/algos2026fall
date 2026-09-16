class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


n = int(input())
values = list(map(int, input().split()))

head = None
tail = None

for value in values:
    node = Node(value)
    if head is None:
        head = node
    else:
        tail.next = node
    tail = node

if n == 1:
    head = None
else:
    current = head
    for i in range(n // 2 - 1):
        current = current.next
    current.next = current.next.next

answers = []
current = head
while current is not None:
    answers.append(current.value)
    current = current.next

print(*answers)
