class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def inserts(head, value, position):
    node = Node(value)

    if position == 0:
        node.next = head
        return node

    current = head
    for i in range(position - 1):
        current = current.next

    node.next = current.next
    current.next = node
    return head


def remove(head, position):
    if position == 0:
        return head.next

    current = head
    for i in range(position - 1):
        current = current.next

    current.next = current.next.next
    return head


def print_list(head):
    if head is None:
        print(-1)
        return

    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next

    print(*values)


def replace(head, first_position, second_position):
    if first_position == second_position:
        return head

    if first_position == 0:
        node = head
        head = head.next
    else:
        current = head
        for i in range(first_position - 1):
            current = current.next
        node = current.next
        current.next = node.next

    if second_position == 0:
        node.next = head
        return node

    current = head
    for i in range(second_position - 1):
        current = current.next

    node.next = current.next
    current.next = node
    return head


def reverse(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def cyclic_left(head, x):
    if head is None or x == 0:
        return head

    tail = head
    while tail.next is not None:
        tail = tail.next

    current = head
    for i in range(x - 1):
        current = current.next

    new_head = current.next
    current.next = None
    tail.next = head
    return new_head


def cyclic_right(head, x):
    if head is None or x == 0:
        return head

    length = 0
    current = head
    while current is not None:
        length = length + 1
        current = current.next

    return cyclic_left(head, length - x)


head = None

while True:
    parts = list(map(int, input().split()))
    command = parts[0]

    if command == 0:
        break
    elif command == 1:
        head = inserts(head, parts[1], parts[2])
    elif command == 2:
        head = remove(head, parts[1])
    elif command == 3:
        print_list(head)
    elif command == 4:
        head = replace(head, parts[1], parts[2])
    elif command == 5:
        head = reverse(head)
    elif command == 6:
        head = cyclic_left(head, parts[1])
    elif command == 7:
        head = cyclic_right(head, parts[1])
