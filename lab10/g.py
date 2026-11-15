def can_remove_edge(graph, incoming):
    size = len(graph)
    queue = []
    for vertex in range(size):
        if incoming[vertex] == 0:
            queue.append(vertex)

    for vertex in queue:
        for neighbor in graph[vertex]:
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                queue.append(neighbor)

    removed = len(queue)
    if removed == size:
        return True

    for start in range(size):
        if incoming[start] != 1:
            continue

        remaining = incoming.copy()
        remaining[start] = 0
        queue = [start]

        for vertex in queue:
            for neighbor in graph[vertex]:
                remaining[neighbor] -= 1
                if remaining[neighbor] == 0:
                    queue.append(neighbor)

        if removed + len(queue) == size:
            return True

    return False


input = open(0).readline
n, m = map(int, input().split())
graph = [[] for vertex in range(n)]
incoming = [0] * n

for edge in range(m):
    first, second = map(int, input().split())
    graph[first - 1].append(second - 1)
    incoming[second - 1] += 1

if can_remove_edge(graph, incoming):
    print("YES")
else:
    print("NO")