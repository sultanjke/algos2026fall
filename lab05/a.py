def minimum_cost(lengths):
    counts = [0] * (max(lengths) + 1)
    for length in lengths:
        counts[length] += 1

    index = 0
    for length in range(1, len(counts)):
        for occurrence in range(counts[length]):
            lengths[index] = length
            index += 1

    combined = []
    original_index = 0
    combined_index = 0
    size = len(lengths)
    total = 0

    for merge_number in range(size - 1):
        merged_length = 0

        for selection in range(2):
            if original_index < size and (
                combined_index == len(combined)
                or lengths[original_index] <= combined[combined_index]
            ):
                merged_length += lengths[original_index]
                original_index += 1
            else:
                merged_length += combined[combined_index]
                combined_index += 1

        combined.append(merged_length)
        total += merged_length

    return total


n = int(input())
lengths = list(map(int, input().split()))
print(minimum_cost(lengths))
