n = int(input()) # 개수
array = [0] * 1000001

# 전체 원소 값에 해당하는 인덱스의 값 1
for i in input().split() :
    array[int(i)] = 1

m = int(input()) # 찾을 원소 개수
x = list(map(int, input().split())) # 찾을 원소

for i in x :
    if array[i] == 1:
        print('yes', end=' ')
    else :
        print('no', end=' ')