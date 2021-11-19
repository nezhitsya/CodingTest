def solution(A, K):
    A_rotate = [0 for _ in range(len(A))] # 리스트 A의 길이만큼의 리스트 생성

    for i in range(len(A)):
        if len(A) == 0: # A의 길이가 0이면 그대로 리턴
            return A
        # i + K가 A 길이를 넘을 경우 맨 앞에서 넘는 길이 만큼 인덱스 이동
        if (i + K) >= len(A):
            A_rotate[i + K - len(A)] = A[i]
        # i + K가 A 길이를 넘지 않을 경우 K만큼 인덱스 이동
        else:
            A_rotate[i + K] = A[i]
        
        # Score 100% 풀이
        # A_rotate[(i + K) % len(A)] = A[i]
        
    return A_rotate

print(solution([3, 8, 9, 7, 6], 1)) # [6, 3, 8, 9, 7]
print(solution([3, 8, 9, 7, 6], 3)) # [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1)) # [0, 0, 0]
print(solution([1, 2, 3, 4], 4)) # [1, 2, 3, 4]