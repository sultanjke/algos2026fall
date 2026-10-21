def build_hashes(text, base, modulo):
    prefix = [0]
    powers = [1]

    for letter in text:
        prefix.append((prefix[-1] * base + ord(letter) - 96) % modulo)
        powers.append(powers[-1] * base % modulo)

    return prefix, powers


def answer_queries(text, queries, query_count):
    modulo_first = 1000000007
    modulo_second = 1000000009
    prefix_first, powers_first = build_hashes(text, 31, modulo_first)
    prefix_second, powers_second = build_hashes(text, 37, modulo_second)
    size = len(text)
    answers = [0] * query_count

    for length in range(1, size + 1):
        if not queries[length]:
            continue

        counts = {}
        power_first = powers_first[length]
        power_second = powers_second[length]

        for start in range(size - length + 1):
            end = start + length
            first = (prefix_first[end] - prefix_first[start] * power_first) % modulo_first
            second = (prefix_second[end] - prefix_second[start] * power_second) % modulo_second
            key = (first, second)
            counts[key] = counts.get(key, 0) + 1

        for start, query_number in queries[length]:
            end = start + length
            first = (prefix_first[end] - prefix_first[start] * power_first) % modulo_first
            second = (prefix_second[end] - prefix_second[start] * power_second) % modulo_second
            answers[query_number] = counts[(first, second)]

    return answers


input = open(0).readline
text = input().strip()
q = int(input())
queries = [[] for length in range(len(text) + 1)]

for query_number in range(q):
    left, right = map(int, input().split())
    length = right - left + 1
    queries[length].append((left - 1, query_number))

answers = answer_queries(text, queries, q)
print("\n".join(map(str, answers)))
