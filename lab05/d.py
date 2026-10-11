def count_operations(densities, target):
    densities.sort()
    combined = []
    original_index = 0
    combined_index = 0
    size = len(densities)
    remaining = size
    operations = 0

    while remaining > 1:
        if original_index < size and (
            combined_index == len(combined)
            or densities[original_index] <= combined[combined_index]
        ):
            first = densities[original_index]
            original_index += 1
        else:
            first = combined[combined_index]
            combined_index += 1

        if first >= target:
            return operations

        if original_index < size and (
            combined_index == len(combined)
            or densities[original_index] <= combined[combined_index]
        ):
            second = densities[original_index]
            original_index += 1
        else:
            second = combined[combined_index]
            combined_index += 1

        combined.append(first + 2 * second)
        operations += 1
        remaining -= 1

    if original_index < size:
        last = densities[original_index]
    else:
        last = combined[combined_index]

    if last < target:
        return -1
    return operations


n, m = map(int, input().split())
densities = list(map(int, input().split()))
print(count_operations(densities, m))
