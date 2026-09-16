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

current = head
while current is not None and current.next is not None:
    current.next = current.next.next
    current = current.next

answers = []
current = head
while current is not None:
    answers.append(current.value)
    current = current.next

print(*answers)
