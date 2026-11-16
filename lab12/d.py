n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
distance = [10**18] * n
distance[0] = 0
used = [False] * n

for _ in range(n):
    vertex = -1
    for candidate in range(n):
        if not used[candidate]:
            if vertex == -1 or distance[candidate] < distance[vertex]:
                vertex = candidate
    if vertex == n - 1:
        break
    used[vertex] = True
    x, y = points[vertex]
    for neighbor in range(n):
        if not used[neighbor]:
            next_x, next_y = points[neighbor]
            weight = abs(x - next_x) + abs(y - next_y)
            needed = max(distance[vertex], weight)
            if needed < distance[neighbor]:
                distance[neighbor] = needed
print(distance[n - 1])
