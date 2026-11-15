def count_islands(field, rows, columns):
    answer = 0
    for row in range(rows):
        for column in range(columns):
            if field[row][column] != "1":
                continue

            answer += 1
            field[row][column] = "0"
            stack = [(row, column)]

            while stack:
                current_row, current_column = stack.pop()
                for next_row, next_column in (
                    (current_row - 1, current_column),
                    (current_row + 1, current_column),
                    (current_row, current_column - 1),
                    (current_row, current_column + 1)
                ):
                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        if field[next_row][next_column] == "1":
                            field[next_row][next_column] = "0"
                            stack.append((next_row, next_column))

    return answer


n, m = map(int, input().split())
field = []
for row in range(n):
    field.append(list("".join(input().split())))

print(count_islands(field, n, m))