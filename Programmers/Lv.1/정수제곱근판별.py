def solution(n):
    answer = 0
    
    if (n ** 0.5).is_integer():
        answer = (n ** 0.5 + 1) ** 2
    else:
        answer = -1
    
    return answer

# def solution(n):
#     return n == int(n ** .5) ** 2 and int(n ** .5 + 1) ** 2 or -1