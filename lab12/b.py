import sys
import heapq

INF = float('inf')
SHIFT = 1 << 17


def dijkstra(start, targets, n, graph):
    push = heapq.heappush  
    pop = heapq.heappop

    dist = [INF] * (n + 1)
    done = [False] * (n + 1)
    dist[start] = 0
    heap = [start]  

    need = set(targets)  

    while heap:
        key = pop(heap)
        v = key % SHIFT
        if done[v]:
            continue 
        done[v] = True

        need.discard(v)
        if not need:
            break  

        d = key // SHIFT
        for to, length in graph[v]:
            new_dist = d + length
            if new_dist < dist[to]:
                dist[to] = new_dist
                push(heap, new_dist * SHIFT + to)

    return dist


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])

    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        v = int(data[idx]); u = int(data[idx + 1]); c = int(data[idx + 2])
        idx += 3
        graph[v].append((u, c))
        graph[u].append((v, c))  

    s = int(data[idx]); a = int(data[idx + 1])
    b = int(data[idx + 2]); f = int(data[idx + 3])

    from_a = dijkstra(a, [s, b, f], n, graph)
    from_b = dijkstra(b, [s, a, f], n, graph)

    route1 = from_a[s] + from_a[b] + from_b[f]  
    route2 = from_b[s] + from_b[a] + from_a[f]  
    answer = min(route1, route2)

    if answer == INF:
        print(-1)
    else:
        print(answer)


main()