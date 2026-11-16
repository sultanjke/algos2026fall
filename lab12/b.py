def push(heap, item):
    heap.append(item)
    position = len(heap) - 1
    while position > 0:
        parent = (position - 1) // 2
        if heap[parent] <= item:
            break
        heap[position] = heap[parent]
        position = parent
    heap[position] = item


def pop(heap):
    answer = heap[0]
    last = heap.pop()
    if not heap:
        return answer
    position = 0
    while position * 2 + 1 < len(heap):
        child = position * 2 + 1
        if child + 1 < len(heap) and heap[child + 1] < heap[child]:
            child += 1
        if last <= heap[child]:
            break
        heap[position] = heap[child]
        position = child
    heap[position] = last
    return answer


def dijkstra(start):
    distance = [10**18] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        current, vertex = pop(heap)
        if current != distance[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            candidate = current + weight
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                push(heap, (candidate, neighbor))
    return distance


input = open(0).readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second, weight = map(int, input().split())
    graph[first].append((second, weight))
    graph[second].append((first, weight))
start, merchant, pharmacy, finish = map(int, input().split())

from_merchant = dijkstra(merchant)
from_pharmacy = dijkstra(pharmacy)
first_route = from_merchant[start] + from_merchant[pharmacy] + from_pharmacy[finish]
second_route = from_pharmacy[start] + from_pharmacy[merchant] + from_merchant[finish]
answer = min(first_route, second_route)
print(answer if answer < 10**18 else -1)
