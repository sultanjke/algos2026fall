input = open(0).readline
n, q = map(int, input().split())
matrix = []

for row in range(n):
    matrix.append(bytearray(map(int, input().split())))

answers = []
for query in range(q):
    first, second, third = map(int, input().split())
    first -= 1
    second -= 1
    third -= 1
    if matrix[first][second] and matrix[first][third] and matrix[second][third]:
        answers.append("YES")
    else:
        answers.append("NO")

print("\n".join(answers))