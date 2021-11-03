def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

# def solution(n, lost, reserve):
#     answer = 0
#     for i in range(1, n+1):
#         if i not in lost: #안 잃어버린 학생
#             answer += 1
#         else:
#             if i in reserve: #잃어버렸지만 여분도 있는 학생
#                 answer += 1
#                 reserve.remove(i)
#                 lost.remove(i)

#     for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
#         if i-1 in reserve:
#             answer += 1
#             reserve.remove(i-1)

#         elif i+1 in reserve:
#             answer +=1
#             reserve.remove(i+1)

#     return answer

# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]

#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)

#     return n - len(_lost)