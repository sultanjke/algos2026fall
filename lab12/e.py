n = int(input())
edges = []
for start in range(n):
    row = list(map(int, input().split()))
    for end in range(n):
        if row[end] != 100000:
            edges.append((start, end, row[end]))

distance = [0] * n
parent = [-1] * n
for _ in range(n):
    changed = -1
    for start, end, weight in edges:
        candidate = distance[start] + weight
        if candidate < distance[end]:
            distance[end] = candidate
            parent[end] = start
            changed = end
    if changed == -1:
        break

if changed == -1:
    print("NO")
else:
    vertex = changed
    for _ in range(n):
        vertex = parent[vertex]
    cycle = [vertex]
    current = parent[vertex]
    while current != vertex:
        cycle.append(current)
        current = parent[current]
    cycle.reverse()
    position = cycle.index(max(cycle))
    cycle = cycle[position:] + cycle[:position]
    cycle.append(cycle[0])
    print("YES")
    print(len(cycle))
    print(*(vertex + 1 for vertex in cycle))
