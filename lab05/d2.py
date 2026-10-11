import sys
from heapq import *
n, m, *h = map(int, sys.stdin.buffer.read().split())
heapify(h)
c = 0
while len(h) > 1 and h[0] < m:
    a = heappop(h)
    heapreplace(h, a + 2 * h[0])
    c += 1
print(c if h[0] >= m else -1)
