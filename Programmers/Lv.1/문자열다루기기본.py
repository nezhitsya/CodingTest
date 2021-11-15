def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False
    if answer == True:
        if s.isdigit():
            answer = True
        else:
            answer = False
    
    return answer

# def solution(s):
#     return s.isdigit() and len(s) in (4, 6)