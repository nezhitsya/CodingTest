def solution(X, Y, D):
    # X에서 Y까지 길이에서 점프할 수 있는 거리 D를 나눈 몫 = 이동 횟수
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return (Y - X) // D + 1

print(solution(10, 85, 30)) # 3