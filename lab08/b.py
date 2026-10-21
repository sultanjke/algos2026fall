def count_shared(first, second, pattern):
    size = min(len(first), len(second))
    length = len(pattern)
    if length > size:
        return 0

    modulo_first = 1000000007
    modulo_second = 1000000009
    target_first = 0
    target_second = 0
    power_first = 1
    power_second = 1

    for letter in pattern:
        value = ord(letter) - 96
        target_first = (target_first * 31 + value) % modulo_first
        target_second = (target_second * 37 + value) % modulo_second
        power_first = power_first * 31 % modulo_first
        power_second = power_second * 37 % modulo_second

    hash_first = 0
    hash_second = 0
    equal_length = 0
    answer = 0

    for index in range(size):
        if first[index] != second[index]:
            hash_first = 0
            hash_second = 0
            equal_length = 0
            continue

        value = ord(first[index]) - 96
        hash_first = (hash_first * 31 + value) % modulo_first
        hash_second = (hash_second * 37 + value) % modulo_second
        equal_length += 1

        if equal_length > length:
            previous = ord(first[index - length]) - 96
            hash_first = (hash_first - previous * power_first) % modulo_first
            hash_second = (hash_second - previous * power_second) % modulo_second

        if equal_length >= length and hash_first == target_first and hash_second == target_second:
            answer += 1

    return answer


first = input().strip()
second = input().strip()
pattern = input().strip()
print(count_shared(first, second, pattern))
