n = int(input())
left = [0] * (n + 1)
right = [0] * (n + 1)

for edge_number in range(n - 1):
    parent, child, side = map(int, input().split())
    if side == 0:
        left[parent] = child
    else:
        right[parent] = child

level = [1]
width = 0

while level:
    width = max(width, len(level))
    next_level = []

    for node in level:
        if left[node] != 0:
            next_level.append(left[node])
        if right[node] != 0:
            next_level.append(right[node])

    level = next_level

print(width)
