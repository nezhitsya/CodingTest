def solution(priorities, location):
    answer = 0
    
    while len(priorities) != 0:
        if location == 0: # 요청 문서가 맨 앞에 위치
            if priorities[0] < max(priorities): # 더 중요도가 큰 문서 존재 시
                priorities.append(priorities.pop(0)) # 맨 뒤 이동 후
                location = len(priorities) - 1 # 요청 문서 위치 맨 뒤로 조정
            else:
                return answer + 1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location -= 1 # 맨 앞 요소가 뒤로 이동하여 위치 -1 이동
            else:
                priorities.pop(0)
                location -= 1
                answer += 1
        
    return answer

# def solution(priorities, location):
#     queue =  [(i, p) for i, p in enumerate(priorities)]
#     answer = 0

#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer