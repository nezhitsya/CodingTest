n = int(input()) # 개수
array = set(map(int, input().split())) # 전체 원소 집합 자료형(set)에 기록

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in array :
        print('yes', end=' ')
    else :
        print('no', end=' ')