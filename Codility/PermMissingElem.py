def solution(A):
    # 1 부터 A 길이 + 1까지 탐색
    for i in range(1, len(A) + 2):
        if i not in A:
            return i
    
    # Score 100% 풀이
    # if len(A) == 0:
    #     return 1
    # return sum(range(1, len(A) + 2)) - sum(A)

print(solution([]))
print(solution([2, 3, 1, 5]))