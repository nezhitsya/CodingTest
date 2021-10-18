import sys

read = sys.stdin.readline
n = int(read())
stair = [0] + [int(read()) for _ in range(n)] + [0]
cache = [0] * (n + 2)
cache[1] = stair[1]
cache[2] = cache[1] + stair[2]

for i in range(3, n + 1):
    cache[i] = max(cache[i - 2], cache[i - 3] + stair[i - 1]) + stair[i]

print(cache[n])