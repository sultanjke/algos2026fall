n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
used = [False] * n
distance = [10**9] * n
distance[0] = 0
answer = 0

for _ in range(n):
    vertex = -1
    for candidate in range(n):
        if not used[candidate]:
            if vertex == -1 or distance[candidate] < distance[vertex]:
                vertex = candidate
    used[vertex] = True
    answer += distance[vertex]
    for neighbor in range(n):
        if not used[neighbor] and cost[vertex][neighbor] < distance[neighbor]:
            distance[neighbor] = cost[vertex][neighbor]
print(answer)
