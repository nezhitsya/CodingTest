def solution(N):
    binary = [] # 2진법 수를 리스트로 저장
    gap = 0 # 1과 1 사이 0 갯수
    gaps = [] # gap 값을 저장하는 리스트

    # 2진법 수행
    while N > 0:
        binary.append(N % 2)
        N //= 2
    
    # binary 리스트를 뒤에서부터 탐색
    for i in reversed(binary):
        # 1이면 지금까지의 0의 갯수를 리스트에 저장 후 0으로 초기화
        if i == 1:
            gaps.append(gap)
            gap = 0
        # 0이면 0의 갯수 1씩 증가
        else:
            gap += 1
    return max(gaps)

print(solution(9)) # 2
print(solution(529)) # 4
print(solution(20)) # 1
print(solution(15)) # 0
print(solution(32)) # 0
print(solution(1041)) # 5