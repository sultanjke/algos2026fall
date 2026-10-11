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


n = int(input())
points = radix_sort(list(map(int, input().split())))
smallest = points[1] - points[0]

for index in range(1, n):
    difference = points[index] - points[index - 1]
    if difference < smallest:
        smallest = difference

answer = []
for index in range(1, n):
    if points[index] - points[index - 1] == smallest:
        answer.append(str(points[index - 1]))
        answer.append(str(points[index]))

print(" ".join(answer))
