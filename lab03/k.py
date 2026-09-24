t = int(input())
queries = list(map(int, input().split()))
n, m = map(int, input().split())

matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

for target in queries:
    left = 0
    right = n * m - 1
    found = False

    while left <= right:
        middle = (left + right) // 2
        row = middle // m
        column = middle % m

        if row % 2 == 1:
            column = m - 1 - column

        value = matrix[row][column]

        if value == target:
            print(row, column)
            found = True
            break
        elif value > target:
            left = middle + 1
        else:
            right = middle - 1

    if not found:
        print(-1)
