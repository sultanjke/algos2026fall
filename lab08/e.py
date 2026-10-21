def build_hashes(text, base, modulo):
    prefix = [0]
    powers = [1]

    for letter in text:
        prefix.append((prefix[-1] * base + ord(letter) - 96) % modulo)
        powers.append(powers[-1] * base % modulo)

    return prefix, powers


def count_distinct(text):
    modulo_first = 1000000007
    modulo_second = 1000000009
    prefix_first, powers_first = build_hashes(text, 31, modulo_first)
    prefix_second, powers_second = build_hashes(text, 37, modulo_second)
    size = len(text)
    answer = 0

    for length in range(1, size + 1):
        seen = set()
        power_first = powers_first[length]
        power_second = powers_second[length]

        for start in range(size - length + 1):
            end = start + length
            first = (prefix_first[end] - prefix_first[start] * power_first) % modulo_first
            second = (prefix_second[end] - prefix_second[start] * power_second) % modulo_second
            seen.add((first, second))

        answer += len(seen)

    return answer


text = open(0).readline().strip()
print(count_distinct(text))
