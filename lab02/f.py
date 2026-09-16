class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    head = None
    tail = None

    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node

    return head


first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))

first = build_list(first_line[1:])
second = build_list(second_line[1:])
head = None
tail = None

while first is not None and second is not None:
    if first.value <= second.value:
        node = first
        first = first.next
    else:
        node = second
        second = second.next

    if head is None:
        head = node
    else:
        tail.next = node
    tail = node

if first is not None:
    remaining = first
else:
    remaining = second

if head is None:
    head = remaining
else:
    tail.next = remaining

answers = []
current = head
while current is not None:
    answers.append(current.value)
    current = current.next

print(*answers)
