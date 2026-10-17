def count_inversions(values):
    size = len(values)
    if size <= 1:
        return values, 0

    middle = size // 2
    left, left_count = count_inversions(values[:middle])
    right, right_count = count_inversions(values[middle:])
    inversions = left_count + right_count
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
            inversions += left_size - left_index

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged, inversions


n = int(input())
numbers = list(map(int, input().split()))
numbers, inversions = count_inversions(numbers)
print(inversions)
