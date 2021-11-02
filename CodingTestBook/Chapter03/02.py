n, m, k = map(int, input().split()) # n개의 자연수 중, m번 더하여 가장 큰 수. 중복은 k번까지 가능
data = list(map(int, input().split()))

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k) :
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
