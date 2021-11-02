n, m = map(int, input().split()) # 개수, 길이
array = list(map(int, input().split())) # 개별 길이

start = 0
end = max(array)
result = 0

while(start <= end) :
    total = 0
    mid = (start + end) // 2
    for x in array :
        # 자르고 남은 길이
        if x > mid :
            total += x - mid
    if total < m :
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)