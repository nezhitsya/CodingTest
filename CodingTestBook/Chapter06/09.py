n, k = map(int, input().split()) # n개 원소 k번 바꿔치기 연산 수행
a = list(map(int, input().split()))  # 모든 원소 합 최대
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break

print(sum(a))