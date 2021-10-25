size = int(input())
pole = [[*map(int, input().split())] for _ in range(size)]
pole.sort(key=lambda x: x[0])

dp = [0] * size

for i in range(size):
    temp = 0
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            temp = max(temp, dp[j])
    
    dp[i] = temp + 1

print(size - max(dp))