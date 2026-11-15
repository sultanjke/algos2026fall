import sys
n, m, *x = map(int, sys.stdin.buffer.read().split())
g = [[] for _ in range(n + 1)]
for i in range(0, 2 * m, 2):
    g[x[i]].append(x[i + 1])
    g[x[i + 1]].append(x[i])
seen = [False] * (n + 1)
ans = 0
for r in range(1, n + 1):
    if not seen[r]:
        seen[r] = True
        ans += 1
        q = [(r, len(g[r]))]
        for v, kids in q:
            for u in g[v]:
                if not seen[u]:
                    seen[u] = True
                    ans += len(g[u]) - 1 > kids
                    q.append((u, len(g[u]) - 1))
print(ans)