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

current_sum = head.value
best_sum = head.value
current = head.next

while current is not None:
    if current_sum < 0:
        current_sum = current.value
    else:
        current_sum = current_sum + current.value

    if current_sum > best_sum:
        best_sum = current_sum

    current = current.next

print(best_sum)
