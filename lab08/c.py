def count_patterns(patterns, text):
    children = [{}]
    endings = {}

    for pattern in patterns:
        node = 0
        for letter in pattern:
            if letter not in children[node]:
                children[node][letter] = len(children)
                children.append({})
            node = children[node][letter]
        endings[pattern] = node

    links = [0] * len(children)
    counts = [0] * len(children)
    queue = []

    for child in children[0].values():
        queue.append(child)

    for node in queue:
        for letter, child in children[node].items():
            parent = links[node]
            while parent != 0 and letter not in children[parent]:
                parent = links[parent]
            links[child] = children[parent].get(letter, 0)
            queue.append(child)

    node = 0
    for letter in text:
        while node != 0 and letter not in children[node]:
            node = links[node]
        node = children[node].get(letter, 0)
        counts[node] += 1

    for node in reversed(queue):
        counts[links[node]] += counts[node]

    frequencies = {}
    for pattern, node in endings.items():
        frequencies[pattern] = counts[node]

    return frequencies


input = open(0).readline
answers = []

while True:
    n = int(input())
    if n == 0:
        break

    patterns = []
    for pattern_number in range(n):
        patterns.append(input().strip())
    text = input().strip()
    frequencies = count_patterns(patterns, text)
    highest = max(frequencies.values())
    answers.append(str(highest))

    for pattern in patterns:
        if frequencies[pattern] == highest:
            answers.append(pattern)

print("\n".join(answers))
