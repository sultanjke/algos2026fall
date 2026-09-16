class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


n, k = map(int, input().split())
words = input().split()

head = None
tail = None

for word in words:
    node = Node(word)
    if head is None:
        head = node
    else:
        tail.next = node
    tail = node

current = head
for i in range(k - 1):
    current = current.next

new_head = current.next
current.next = None
tail.next = head
head = new_head

answers = []
current = head
while current is not None:
    answers.append(current.value)
    current = current.next

print(*answers)
