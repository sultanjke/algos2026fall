n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

start, finish = map(int, input().split())
distance = [-1] * n
distance[start - 1] = 0
queue = [start - 1]

for vertex in queue:
    if vertex == finish - 1:
        break
    for neighbor in range(n):
        if matrix[vertex][neighbor] == 1 and distance[neighbor] == -1:
            distance[neighbor] = distance[vertex] + 1
            queue.append(neighbor)

print(distance[finish - 1])