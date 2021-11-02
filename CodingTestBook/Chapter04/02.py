n = int(input())

count = 0

# 0 부터 n까지 탐색
for i in range(n + 1) :
    # 0 부터 59까지 탐색
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                count += 1

print(count)