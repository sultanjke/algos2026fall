def find(vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex


input = open(0).readline
n, m = map(int, input().split())
segments = []
for _ in range(m):
    left, right, cost = map(int, input().split())
    segments.append((cost, left, right))
segments.sort()

parent = list(range(n + 1))
answer = 0
for cost, left, right in segments:
    vertex = find(left)
    while vertex < right:
        answer += cost
        parent[vertex] = find(vertex + 1)
        vertex = parent[vertex]
print(answer)
