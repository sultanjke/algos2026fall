t = int(input())

for test in range(t):
    n = int(input())
    deck = [0] * n
    positions = list(range(n))
    index = 0

    for card in range(1, n + 1):
        index = (index + card) % len(positions)
        position = positions.pop(index)
        deck[position] = card

    print(*deck)
