def find_occurrences(text, pattern):
    prefix = [0] * len(pattern)
    matched = 0

    for index in range(1, len(pattern)):
        while matched > 0 and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched

    positions = []
    matched = 0
    for index, letter in enumerate(text):
        while matched > 0 and letter != pattern[matched]:
            matched = prefix[matched - 1]
        if letter == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            positions.append(index - len(pattern) + 2)
            matched = prefix[matched - 1]

    return positions


text = input().strip()
pattern = input().strip()
positions = find_occurrences(text, pattern)
print(len(positions))
print(" ".join(map(str, positions)))
