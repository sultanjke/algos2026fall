def can_cut(ropes, length, k):
    pieces = 0

    for rope in ropes:
        pieces = pieces + int(rope / length)
        if pieces >= k:
            return True

    return False


n, k = map(int, input().split())
ropes = list(map(int, input().split()))

left = 0.0
right = max(ropes)

for step in range(70):
    middle = (left + right) / 2

    if can_cut(ropes, middle, k):
        left = middle
    else:
        right = middle

print(f"{left:.9f}")
