n, k = map(int, input().split()) # n이 1이 될 때 까지 k로 나누기 or -1

count = 0

while True :
    target = (n // k) * k # target = n에 근접한 k의 배수
    count += (n - target) # n과 target의 차이많큼 -1 연산을 수행함으로 count는 -1 연산 수행 값만큼 추가된다.
    n = target

    if n < k : # n이 k보다 작으면 반복문 탈출
        break
    count += 1
    n //= k

# 마지막 남은 수에서 -1 연산 수행한 횟수 추가
count += (n - 1)
print(result)