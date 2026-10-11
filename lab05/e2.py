import sys
from heapq import *
_, k, *c = sys.stdin.read().split()
k = int(k)
h, t, o, i = [], 0, [], 0
while i < len(c):
    if c[i] == "print":
        o.append(t)
    else:
        i += 1
        v = int(c[i])
        if len(h) < k:
            heappush(h, v); t += v
        elif v > h[0]:
            t += v - heapreplace(h, v)
    i += 1
print(*o, sep="\n")