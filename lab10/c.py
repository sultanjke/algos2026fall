def shortest_path(start, finish):
    limit = 2 * max(start, finish)
    parent = [-1] * (limit + 1)
    parent[start] = start
    queue = [start]

    for number in queue:
        if number == finish:
            break
        for neighbor in (number * 2, number - 1):
            if 1 <= neighbor <= limit and parent[neighbor] == -1:
                parent[neighbor] = number
                queue.append(neighbor)

    path = []
    current = finish
    while current != start:
        path.append(current)
        current = parent[current]

    return path[::-1]


start, finish = map(int, input().split())
path = shortest_path(start, finish)
print(len(path))
if path:
    print(" ".join(map(str, path)))