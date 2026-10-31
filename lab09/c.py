def cyclic_shift(original, changed):
    prefix = [0] * len(original)
    matched = 0

    for index in range(1, len(original)):
        while matched > 0 and original[index] != original[matched]:
            matched = prefix[matched - 1]
        if original[index] == original[matched]:
            matched += 1
        prefix[index] = matched

    matched = 0
    for index, letter in enumerate(changed + changed[:-1]):
        while matched > 0 and letter != original[matched]:
            matched = prefix[matched - 1]
        if letter == original[matched]:
            matched += 1
        if matched == len(original):
            return index - len(original) + 1

    return -1


original = input().strip()
changed = input().strip()
print(cyclic_shift(original, changed))
