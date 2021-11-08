# Time Out
# def solution(scoville, K):
#     answer = 0
    
#     while min(scoville) < K:
#         scoville.sort()
#         try:
#             scoville.append(scoville.pop(0) + scoville.pop(0) * 2)
#         except IndexError:
#             return -1
#         answer += 1
    
#     return answer