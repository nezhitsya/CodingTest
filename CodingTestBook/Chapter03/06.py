n, k = map(int, input().split()) # n이 1이 될 때 까지 k로 나누기 or -1

count = 0

while n >= k : # n이 k 이상일 경우
    while n % k != 0 : # n이 k 이상이지만 k로 나눈 나머지가 0이 아니면
        n -= 1
        count += 1
    n = n // k
    count += 1

while n > 1 : # n이 k보다 작지만 1보다 큰 경우
    n -= 1
    count += 1

print(count)