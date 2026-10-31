def minimum_repetitions(text, pattern):
    prefix = [0] * len(pattern)
    matched = 0

    for index in range(1, len(pattern)):
        while matched > 0 and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched

    matched = 0
    for index in range(len(text) + len(pattern) - 1):
        letter = text[index % len(text)]
        while matched > 0 and letter != pattern[matched]:
            matched = prefix[matched - 1]
        if letter == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            return (index + len(text)) // len(text)

    return -1


text = input().strip()
pattern = input().strip()
print(minimum_repetitions(text, pattern))
