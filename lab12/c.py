def bfs(transport):
    distance = [-1] * n
    distance[0] = 0
    queue = [0]
    head = 0
    while head < len(queue):
        vertex = queue[head]
        head += 1
        for neighbor in range(n):
            if distance[neighbor] == -1 and graph[vertex][neighbor] == transport:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    return distance[n - 1]


input = open(0).readline
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    first, second = map(int, input().split())
    graph[first - 1][second - 1] = 1
    graph[second - 1][first - 1] = 1

flight_time = bfs(1)
road_time = bfs(0)
if flight_time == -1 or road_time == -1:
    print(-1)
else:
    print(max(flight_time, road_time))
