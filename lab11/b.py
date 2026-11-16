n = int(input())
ducks = list(map(int, input().split()))

cheapest = 0
for island in range(n):
    if ducks[island] < ducks[cheapest]:
        cheapest = island

answer = 0
for island in range(n):
    if island != cheapest:
        answer += ducks[cheapest] + ducks[island]
print(answer)
