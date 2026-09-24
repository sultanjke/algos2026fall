n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
found = False

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == x:
        found = True
        break
    elif numbers[middle] < x:
        left = middle + 1
    else:
        right = middle - 1

if found:
    print("Yes")
else:
    print("No")
