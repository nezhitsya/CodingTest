n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1 # 만들 수 있는 금액
for coin in coins :
    if target < coin :
        break
    target += coin

print(target)