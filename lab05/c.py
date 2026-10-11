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


def maximum_income(heap, visitors):
    for index in range(len(heap) // 2 - 1, -1, -1):
        sift_down(heap, index)

    total = 0
    for visitor in range(visitors):
        total += heap[0]
        heap[0] -= 1
        sift_down(heap, 0)

    return total


n, x = map(int, input().split())
seats = list(map(int, input().split()))
print(maximum_income(seats, x))
