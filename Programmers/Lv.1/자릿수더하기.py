def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)

    return answer

# 재귀
# def solution(n):
#     if n < 10:
#         return n
#     return (n % 10) + solution(n // 10)