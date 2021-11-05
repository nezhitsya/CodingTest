def solution(record):
    answer = []
    dict = {}
    
    for i in record:
        i_split = i.split()
        if len(i_split) == 3:
            dict[i_split[1]] = i_split[2]
    
    for i in record:
        i_split = i.split()
        if i_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dict[i_split[1]])
        elif i_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dict[i_split[1]])
    
    return answer

# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

#     return answer