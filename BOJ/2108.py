import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

# 평균
for _ in range(n) :
    arr.append(int(sys.stdin.readline()))
print("%.f"%(sum(arr)/n))

if n == 1 :
    print(arr[0])
    print(arr[0])
    print(0)
    sys.exit()

# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값

# 시간 초과
# count = dict()
# for i in arr :
#     if i in count :
#         count[i] += 1
#     else :
#         count[i] = 1
# max_value = max(count.values())
# max_key = []
# for key in count :
#     if count[key] == max_value :
#         max_key.append(key)
# if len(max_key) > 1 :
#     max_key.sort()
#     print(max_key[1])
# else :
#     print(max_key[0])

cnt = Counter(arr)
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

if cnt[0][1] == cnt[1][1] :
    print(cnt[1][0])
else :
    print(cnt[0][0])

# 범위
print(arr[-1] - arr[0])