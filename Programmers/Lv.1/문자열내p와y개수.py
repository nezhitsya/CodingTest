def solution(s):
    answer = True
    p_count = 0
    y_count = 0

    for i in s.lower():
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1

    if p_count == y_count:
        answer = True
    else:
        answer = False

    return answer

# def solution(s):
#     return s.lower().count('p') == s.lower().count('y')