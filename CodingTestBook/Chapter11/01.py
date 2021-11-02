n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data :
    count += 1 # 현재 그룹에 해당 모험가 포함
    if count >= 1 : # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상인 경우, 그룹 결성
        group += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹에 포함된 모험가 수 초기화

print(group)