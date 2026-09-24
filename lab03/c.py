n, m = map(int, input().split())
blocks = list(map(int, input().split()))

ends = []
total = 0

for length in blocks:
    total = total + length
    ends.append(total)

answers = []

for mistake in range(m):
    line = int(input())
    left = 0
    right = n

    while left < right:
        middle = (left + right) // 2
        if ends[middle] < line:
            left = middle + 1
        else:
            right = middle

    answers.append(str(left + 1))

print("\n".join(answers))
