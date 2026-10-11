def radix_sort(values):
    if len(values) <= 1:
        return values

    smallest = min(values)
    largest_difference = max(values) - smallest
    place = 1
    base = 65536

    while place <= largest_difference:
        counts = [0] * min(base, largest_difference // place + 1)
        for value in values:
            digit = (value - smallest) // place % base
            counts[digit] += 1

        position = 0
        for digit in range(len(counts)):
            amount = counts[digit]
            counts[digit] = position
            position += amount

        ordered = [0] * len(values)
        for value in values:
            digit = (value - smallest) // place % base
            ordered[counts[digit]] = value
            counts[digit] += 1

        values = ordered
        place *= base

    return values


data = list(map(int, open(0).read().split()))
n, m = data[0], data[1]
counts = {}

for value in data[2:n + 2]:
    if value in counts:
        counts[value] += 1
    else:
        counts[value] = 1

answer = []
for value in data[n + 2:n + m + 2]:
    if value in counts and counts[value] > 0:
        answer.append(value)
        counts[value] -= 1

answer = radix_sort(answer)
print(" ".join(map(str, answer)))
