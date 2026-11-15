input = open(0).readline
n, m = map(int, input().split())
graph = [[] for vertex in range(n)]

for edge in range(m):
    first, second = map(int, input().split())
    graph[first - 1].append(second - 1)
    graph[second - 1].append(first - 1)

start, finish = map(int, input().split())
visited = [False] * n
visited[start - 1] = True
queue = [start - 1]

for vertex in queue:
    if vertex == finish - 1:
        break
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

if visited[finish - 1]:
    print("YES")
else:
    print("NO")