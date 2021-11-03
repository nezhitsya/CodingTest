def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for par, com in zip(participant, completion):
        if par != com:
            return par
        
    return participant[-1]

# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]