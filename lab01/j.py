from collections import deque

boris = deque(map(int, input().split()))
nursik = deque(map(int, input().split()))
moves = 0

while boris and nursik:
    first = boris.popleft()
    second = nursik.popleft()

    if first == 0 and second == 9:
        boris_wins = True
    elif first == 9 and second == 0:
        boris_wins = False
    else:
        boris_wins = first > second

    if boris_wins:
        boris.append(first)
        boris.append(second)
    else:
        nursik.append(first)
        nursik.append(second)

    moves = moves + 1

if boris:
    print("Boris", moves)
else:
    print("Nursik", moves)
