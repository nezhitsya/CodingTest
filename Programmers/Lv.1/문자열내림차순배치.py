def solution(s):
    answer = ''.join(i for i in sorted(s, reverse = True))
    return answer

# def solution(s):
#     return ''.join(sorted(s, reverse=True))