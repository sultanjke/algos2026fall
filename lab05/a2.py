from heapq import *
input()
h = list(map(int, input().split()))
heapify(h)
t = 0
while len(h) > 1:
    s = heappop(h) + heappop(h)
    t += s
    heappush(h, s)
print(t)

