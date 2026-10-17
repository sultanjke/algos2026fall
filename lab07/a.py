def merge_sort(words):
    size = len(words)
    if size <= 1:
        return words

    middle = size // 2
    left = merge_sort(words[:middle])
    right = merge_sort(words[middle:])
    merged = []
    left_index = 0
    right_index = 0
    left_size = len(left)
    right_size = len(right)

    while left_index < left_size and right_index < right_size:
        if len(left[left_index]) <= len(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


input = open(0).readline
t = int(input())
answers = []

for set_number in range(t):
    words = input().split()
    words = merge_sort(words)
    answers.append(" ".join(words))

print("\n".join(answers))
