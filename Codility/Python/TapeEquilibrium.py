def solution(A):
    # 절대값을 저장하는 리스트
    A_sum = list()

    # 0 부터 (A 길이 -1) 까지 인덱스 탐색
    for i in range(1, len(A)):
        A_sum.append(abs(sum(A[:i]) - sum(A[i:])))

    return min(A_sum)

    # Score 100% 풀이
    # best = None
    # before = 0
    # after = sum(A)

    # for i in range(0, len(A) - 1):
    #     before += A[i] # 0부터 i까지 합
    #     after -= A[i] # (i + 1)부터 마지막 인덱스까지 합
    #     difference  = abs(before - after)

    #     best 값이 없거나 더 작은 값이 나왔을 경우
    #     if best is None or difference < best:
    #         best = difference
    # return best

print(solution([3, 1, 2, 4, 3])) # 1