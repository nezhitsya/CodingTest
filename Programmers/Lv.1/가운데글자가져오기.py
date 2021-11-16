def solution(s):
    answer = ''
    center = len(s) // 2
    
    if len(s) % 2 != 0:
        answer = s[center]
    else:
        answer = s[center - 1: center + 1]
        
    return answer

# def solution(str):
#     return str[(len(str) - 1) // 2 : len(str) // 2 + 1]