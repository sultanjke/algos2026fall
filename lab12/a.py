def solve():
    input = open(0).readline
    n = int(input())
    distance = [list(map(int, input().split())) for _ in range(n)]
    order = [int(vertex) - 1 for vertex in input().split()]
    active = []
    answers = []

    for added in order:
        active.append(added)
        through = distance[added]
        for start in range(n):
            row = distance[start]
            first_part = row[added]
            for end in range(n):
                candidate = first_part + through[end]
                if candidate < row[end]:
                    row[end] = candidate

        longest = 0
        for start in active:
            row = distance[start]
            for end in active:
                if row[end] > longest:
                    longest = row[end]
        answers.append(longest)
    print(*answers, sep="\n")


solve()
