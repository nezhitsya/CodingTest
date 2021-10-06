import sys
n = int(sys.stdin.readline())
memo = {1:1, 2:1, 3:1, 4:2, 5:2}

def result(number: int) -> int:
    if number in memo:
        return memo[number]
    memo[number] = result(number - 1) + result(number - 5)
    return memo[number]

for _ in range(n):
    num = int(sys.stdin.readline())
    print(result(num))