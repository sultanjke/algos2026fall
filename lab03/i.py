def can_split(houses, limit, k):
    blocks = 1
    total = 0

    for house in houses:
        if total + house > limit:
            blocks = blocks + 1
            total = house
        else:
            total = total + house

        if blocks > k:
            return False

    return True


n, k = map(int, input().split())
houses = list(map(int, input().split()))

left = max(houses)
right = sum(houses)

while left < right:
    middle = (left + right) // 2

    if can_split(houses, middle, k):
        right = middle
    else:
        left = middle + 1

print(left)
