def can_fit(sizes, side, k):
    count = 0

    for size in sizes:
        if size <= side:
            count = count + 1
        if count >= k:
            return True

    return False


n, k = map(int, input().split())
sizes = []

for sheep in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    sizes.append(max(x2, y2))

left = 1
right = max(sizes)

while left < right:
    middle = (left + right) // 2

    if can_fit(sizes, middle, k):
        right = middle
    else:
        left = middle + 1

print(left)
