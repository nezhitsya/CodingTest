def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time * speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)
    return answer

# def solution(progresses, speeds):
#     answer = []
#     for p, s in zip(progresses, speeds):
#         if len(answer) == 0 or answer[-1][0] < -((p-100) // s):
#             answer.append([-((p - 100) // s), 1])
#         else:
#             answer[-1][1] += 1
#     return [q[1] for q in answer]