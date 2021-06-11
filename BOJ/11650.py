n = int(input())
arr = []

for i in range(n) :
    xy = list(map(int, input().split()))
    arr.append(xy)

arr.sort()
for x, y in arr :
    print(x, y)