import sys
from heapq import heappop, heappush
n, m, *x = map(int, sys.stdin.buffer.read().split())
g = [[] for _ in range(n + 1)]
d = [0] * (n + 1)
for i in range(0, 2 * m, 2):
    g[x[i]].append(x[i + 1])
    d[x[i + 1]] += 1
h = [v for v in range(1, n + 1) if d[v] == 0]
order = []
while h:
    v = heappop(h)
    order.append(v)
    for u in g[v]:
        d[u] -= 1
        if d[u] == 0:
            heappush(h, u)
if len(order) == n:
    print("Possible")
    print(*order)
else:
    print("Impossible")