def insert(heap, value):
    heap.append(value)
    index = len(heap) - 1

    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] <= value:
            break
        heap[index] = heap[parent]
        index = parent

    heap[index] = value


def sift_down(heap, index):
    size = len(heap)
    value = heap[index]
    child = 2 * index + 1

    while child < size:
        if child + 1 < size and heap[child + 1] < heap[child]:
            child += 1
        if value <= heap[child]:
            break
        heap[index] = heap[child]
        index = child
        child = 2 * index + 1

    heap[index] = value


input = open(0).readline
q, k = map(int, input().split())
heap = []
total = 0
answers = []

for query in range(q):
    command = input().split()

    if command[0] == "print":
        answers.append(str(total))
    else:
        value = int(command[1])
        if len(heap) < k:
            insert(heap, value)
            total += value
        elif value > heap[0]:
            total += value - heap[0]
            heap[0] = value
            sift_down(heap, 0)

if answers:
    print("\n".join(answers))
