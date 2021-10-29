n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(len(arr) - 1):
    dp.append(max(dp[i] + arr[i + 1], arr[i + 1]))

print(max(dp))