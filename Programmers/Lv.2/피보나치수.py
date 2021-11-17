def solution(n):
    answer = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            answer.append(i)
        else:
            f = answer[i - 1] + answer[i - 2]
            answer.append(f % 1234567)

    return answer[-1]

# Error
# def solution(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# Time Out
# def solution(n):
#     if n < 2:
#         return n
#     else:
#         return (solution(n - 1) + solution(n - 2)) % 1234567