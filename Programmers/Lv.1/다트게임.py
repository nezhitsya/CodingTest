def solution(dartResult):
    answer = []
    n = ''
    
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            answer.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            answer.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            answer.append(n)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1
        
    return sum(answer)

# import re

# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i - 1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer