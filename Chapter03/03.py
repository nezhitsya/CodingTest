n, m, k = map(int, input().split()) # n개의 자연수 중, m번 더하여 가장 큰 수. 중복은 k번까지 가능
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# count = (횟수 / (연속 first + 1번 second)) * 연속 + (횟수 / (연속 + 1번)의 나머지)
# count = first가 연속으로 더해질 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)