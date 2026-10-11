n = int(input())
letters = input().split()
target = input().strip()
left = 0
right = n

while left < right:
    middle = (left + right) // 2
    if letters[middle] <= target:
        left = middle + 1
    else:
        right = middle

if left == n:
    print(letters[0])
else:
    print(letters[left])
