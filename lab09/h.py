def count_splits(text):
    size = len(text)
    limit = (size - 1) // 2
    matches = [0] * (limit + 1)
    left = 0
    right = 0
    answer = 0

    for index in range(1, limit + 1):
        length = 0
        if index < right:
            length = min(right - index, matches[index - left])

        while index + length < size and text[length] == text[index + length]:
            length += 1

        matches[index] = length
        if index + length > right:
            left = index
            right = index + length
        if length >= index:
            answer += 1

    return answer


text = input().strip()
print(count_splits(text))
