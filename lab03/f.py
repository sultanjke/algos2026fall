n, h = map(int, input().split())
bags = list(map(int, input().split()))

left = 1
right = max(bags)

while left < right:
    middle = (left + right) // 2
    hours = 0

    for bag in bags:
        hours = hours + (bag + middle - 1) // middle
        if hours > h:
            break

    if hours <= h:
        right = middle
    else:
        left = middle + 1

print(left)
