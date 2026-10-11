def quick_sort(values):
    stack = [(0, len(values) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = values[(left + right) // 2]
        first = left
        second = right

        while first <= second:
            while values[first] < pivot:
                first += 1
            while values[second] > pivot:
                second -= 1
            if first <= second:
                values[first], values[second] = values[second], values[first]
                first += 1
                second -= 1

        if left < second:
            stack.append((left, second))
        if first < right:
            stack.append((first, right))


n, m = map(int, input().split())
matrix = []

for row in range(n):
    matrix.append(list(map(int, input().split())))

for column in range(m):
    values = []
    for row in range(n):
        values.append(matrix[row][column])

    quick_sort(values)

    for row in range(n):
        matrix[row][column] = values[n - row - 1]

for row in matrix:
    print(*row)
