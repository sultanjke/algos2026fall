def merge_sort(rows):
    size = len(rows)
    if size <= 1:
        return rows

    middle = size // 2
    left = merge_sort(rows[:middle])
    right = merge_sort(rows[middle:])
    merged = []
    left_index = 0
    right_index = 0
    left_size = len(left)
    right_size = len(right)

    while left_index < left_size and right_index < right_size:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


n, m = map(int, input().split())
rows = []

for row_number in range(n):
    row = list(map(int, input().split()))
    rows.append((-sum(row), row))

rows = merge_sort(rows)
answers = []

for negative_sum, row in rows:
    answers.append(" ".join(map(str, row)))

print("\n".join(answers))
