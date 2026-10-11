from heapq import *
n, x = map(int, input().split())
h = [-a for a in map(int, input().split())]
heapify(h)
t = 0
for _ in range(x):
    t -= h[0]
    heapreplace(h, h[0] + 1)
print(t)
