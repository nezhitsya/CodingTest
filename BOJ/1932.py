import sys
read = sys.stdin.readline
n = int(read())
route = [list(map(int, read().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            route[i][j] += route[i - 1][0]
        elif j == i:
            route[i][j] += route[i - 1][-1]
        else:
            route[i][j] += max(route[i - 1][j - 1], route[i - 1][j])

print(max(route[-1]))