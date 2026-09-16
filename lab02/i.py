class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


head = None
tail = None

while True:
    parts = input().split()
    command = parts[0]

    if command == "add_front":
        node = Node(parts[1])
        node.next = head

        if head is None:
            tail = node
        else:
            head.previous = node

        head = node
        print("ok")

    elif command == "add_back":
        node = Node(parts[1])
        node.previous = tail

        if tail is None:
            head = node
        else:
            tail.next = node

        tail = node
        print("ok")

    elif command == "erase_front":
        if head is None:
            print("error")
        else:
            print(head.value)
            head = head.next
            if head is None:
                tail = None
            else:
                head.previous = None

    elif command == "erase_back":
        if tail is None:
            print("error")
        else:
            print(tail.value)
            tail = tail.previous
            if tail is None:
                head = None
            else:
                tail.next = None

    elif command == "front":
        if head is None:
            print("error")
        else:
            print(head.value)

    elif command == "back":
        if tail is None:
            print("error")
        else:
            print(tail.value)

    elif command == "clear":
        while head is not None:
            next_node = head.next
            head.next = None
            head.previous = None
            head = next_node
        tail = None
        print("ok")

    elif command == "exit":
        print("goodbye")
        break
