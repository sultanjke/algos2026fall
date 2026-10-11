def sift_down(heap, index):
    size = len(heap)
    value = heap[index]
    child = 2 * index + 1

    while child < size:
        if child + 1 < size and heap[child + 1] > heap[child]:
            child += 1
        if value >= heap[child]:
            break
        heap[index] = heap[child]
        index = child
        child = 2 * index + 1

    heap[index] = value


def extract_max(heap):
    maximum = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        sift_down(heap, 0)
    return maximum


def remaining_weight(heap):
    for index in range(len(heap) // 2 - 1, -1, -1):
        sift_down(heap, index)

    while len(heap) > 1:
        first = extract_max(heap)
        difference = first - heap[0]

        if difference == 0:
            extract_max(heap)
        else:
            heap[0] = difference
            sift_down(heap, 0)

    if heap:
        return heap[0]
    return 0


n = int(input())
weights = list(map(int, input().split()))
print(remaining_weight(weights))