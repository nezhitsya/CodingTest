n, m = map(int, input().split()) # n행 m열

result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value) # 각 행의 가장 작은 수 중 가장 큰 수

print(result)