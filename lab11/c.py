def find(vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex


input = open(0).readline
n, m = map(int, input().split())
big, small = map(int, input().split())
edges = []
for _ in range(m):
    kind, start, end, length = input().split()
    if kind == "big":
        price = big
    elif kind == "small":
        price = small
    else:
        price = min(big, small)
    edges.append((int(length) * price, int(start), int(end)))
edges.sort()

parent = list(range(n + 1))
size = [1] * (n + 1)
answer = 0
chosen = 0
for cost, start, end in edges:
    first = find(start)
    second = find(end)
    if first != second:
        if size[first] < size[second]:
            first, second = second, first
        parent[second] = first
        size[first] += size[second]
        answer += cost
        chosen += 1
print(answer if chosen == n - 1 else -1)
