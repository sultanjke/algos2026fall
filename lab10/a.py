def spread(field, queue, mushrooms, width):
    minutes = 0
    start = 0

    while start < len(queue) and mushrooms > 0:
        end = len(queue)
        while start < end:
            position = queue[start]
            start += 1
            for neighbor in (position - 1, position + 1, position - width, position + width):
                if field[neighbor] == 1:
                    field[neighbor] = 2
                    mushrooms -= 1
                    queue.append(neighbor)
        minutes += 1

    if mushrooms > 0:
        return -1
    return minutes


input = open(0).readline
rows, columns = map(int, input().split())
width = columns + 2
field = bytearray((rows + 2) * width)
queue = []
mushrooms = 0

for row in range(1, rows + 1):
    for column, value in enumerate(map(int, input().split()), 1):
        position = row * width + column
        field[position] = value
        if value == 1:
            mushrooms += 1
        elif value == 2:
            queue.append(position)

print(spread(field, queue, mushrooms, width))