n, m = map(int, input().split()) # 개수, 최대 무게
data = list(map(int, input().split())) # 무게 리스트

# 각 무게에 해당하는 개수 카운트
array = [0] * 11
for x in data :
    array[x] += 1

result = 0
for i in range(1, m + 1) :
    n -= array[i]
    result += array[i] * n

print(result)