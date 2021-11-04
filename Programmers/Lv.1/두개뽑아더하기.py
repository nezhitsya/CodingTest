def solution(numbers):
    answer = []
    
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()
    
    return answer

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))