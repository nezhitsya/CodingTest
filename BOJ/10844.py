stair = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1:
            stair[i][j] = 1
        else:
            if 1 <= j <= 8:
                stair[i][j] = stair[i - 1][j - 1] + stair[i - 1][j + 1]
            elif j == 0:
                stair[i][j] = stair[i - 1][j + 1]
            elif j == 9:
                stair[i][j] = stair[i - 1][j - 11]

n = int(input())
print(sum(stair[n][1:10]) % 1000000000)