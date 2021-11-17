def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse = True)

    return sum([a * b for a, b in zip(A, B)])

# def solution(A,B):
#     return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse = True)))