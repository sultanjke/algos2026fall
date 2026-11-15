def paint_red(graph, distance, vertex):
    if distance[vertex] == 0:
        return

    distance[vertex] = 0
    queue = [vertex]
    for current in queue:
        next_distance = distance[current] + 1
        for neighbor in graph[current]:
            if next_distance < distance[neighbor]:
                distance[neighbor] = next_distance
                queue.append(neighbor)


input = open(0).readline
n, m, q = map(int, input().split())
graph = [[] for vertex in range(n)]

for edge in range(m):
    first, second = map(int, input().split())
    graph[first - 1].append(second - 1)
    graph[second - 1].append(first - 1)

distance = [n + 1] * n
answers = []

for query in range(q):
    kind, vertex = map(int, input().split())
    vertex -= 1
    if kind == 1:
        paint_red(graph, distance, vertex)
    elif distance[vertex] == n + 1:
        answers.append("-1")
    else:
        answers.append(str(distance[vertex]))

if answers:
    print("\n".join(answers))