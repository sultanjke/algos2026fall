def find(vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex


input = open(0).readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

parent = list(range(n + 1))
size = [1] * (n + 1)
active = [False] * (n + 1)
answers = [0] * n
components = 0
for vertex in range(n, 0, -1):
    answers[vertex - 1] = components
    active[vertex] = True
    components += 1
    for neighbor in graph[vertex]:
        if active[neighbor]:
            first = find(vertex)
            second = find(neighbor)
            if first != second:
                if size[first] < size[second]:
                    first, second = second, first
                parent[second] = first
                size[first] += size[second]
                components -= 1
print(*answers, sep="\n")
