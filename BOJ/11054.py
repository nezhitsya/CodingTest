n = int(input())
a = list(map(int, input().split()))
ar = a[::-1]

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
result = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if ar[i] > ar[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(n):
    result[i] = increase[i] + decrease[n - i - 1] - 1

print(max(result))