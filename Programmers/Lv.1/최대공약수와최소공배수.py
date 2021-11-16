import math

def solution(n, m):
    return [math.gcd(n, m), n * m / math.gcd(n, m)]

# def solution(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1

#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a * b / c)]

#     return answer