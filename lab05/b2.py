from heapq import *
input()
h = [-x for x in map(int, input().split())]
heapify(h)
while len(h) > 1:
    y = heappop(h)
    d = heappop(h) - y
    if d:
        heappush(h, -d)
print(-h[0] if h else 0)